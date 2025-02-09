# comp_run_q_arb_ex.py

import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
from queue_utils import SmartQUtils
from icecream  import ic

class CompRunQArbEx(threading.Thread,SmartQUtils):
    def __init__(self, config, system_config, set_completion_ev):
        # Initialize parent classes
        threading.Thread.__init__(self)  # Initialize threading.Thread
        SmartQUtils.__init__(self, verbose=False)  # Initialize SmartQUtils
    _max_timeout = 0 
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''
    _wait_queue = None
    _run_queue = None
    _done_queue = None
    _name = ''

    def __init__(self, config, system_config,set_completion_ev):
        super().__init__()
        self.config = config
        self.timeout_triggered = False
        self.set_completion_ev = set_completion_ev

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_makefile_path(self, makefile_path):
        self._makefile_path = makefile_path

    def get_makefile_path(self):
        return self._makefile_path

    def set_max_concurrent_task(self, max_concurrent_task):
        self._max_concurrent_task = max_concurrent_task

    def get_max_concurrent_task(self):
        return self._max_concurrent_task

    def set_wait_queue(self, wait_queue):
        self._wait_queue = wait_queue

    def get_wait_queue(self):
        return self._wait_queue

    def set_run_queue(self, run_queue):
        self._run_queue = run_queue

    def get_run_queue(self):
        return self._run_queue

    def set_done_queue(self, done_queue):
        self._done_queue = done_queue

    def get_done_queue(self):
        return self._done_queue

    def run(self):
        try:
            if not self._makefile_path:
                raise ValueError("Missing makefile path in system configuration")

            if not (self._wait_queue is not None and self._run_queue is not None and self._done_queue is not None):
                raise ValueError("Queues not properly set up")

            while not self.config.compile_eot and not self.config.watchdog_eot :
                size = self._run_queue.get_size()
                if size < self.get_max_concurrent_task():
                    if not self._wait_queue.is_empty():
                        self.process_task()
                else:
                    if self._run_queue.is_empty() and self._wait_queue.is_empty() and not self._done_queue.is_empty():
                        if self.set_completion_ev :
                            self.set_completion_ev.set()
                        self.config.compile_eot = True

        except ValueError as CompRunQArbEx_error:
            print(f"{self._name}:: Error in CompRunQArbEx: {CompRunQArbEx_error}")
            os._exit(1)

    def process_task(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            task = self._wait_queue.peek()
            if 'command' in task:
                run_command = task['command']
            else:
                raise ValueError("wait queue does not contain a 'command' key")

            if 'approved' in task:
                #approved = task['approved']
                approved= self.get_approved(task)
            else:
                raise ValueError("wait queue does not contain an 'approved' key")
            if 'status' in task:
                #status = task['status']
                status = self.get_status(task)
            if len(approved) == 0 and status == 'execute':
                task = self._wait_queue.get()
                subdir = os.path.join(self.config.root_dir, task['subdir'])
                os.makedirs(subdir, exist_ok=True)
                if os.path.isdir(self._makefile_path):
                    for filename in os.listdir(self._makefile_path):
                        full_file_path = os.path.join(self._makefile_path, filename)
                        shutil.copy(full_file_path, subdir)
                else:
                    shutil.copy(self._makefile_path, subdir)

                future = executor.submit(subprocess.run, run_command.split(), cwd=subdir)
                task['status'] = 'run'
                task['future'] = future
                self._run_queue.put(task)

