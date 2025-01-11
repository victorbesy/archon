# artifact_run_q_arb_ex.py

import os
import shutil
import subprocess
import threading
import concurrent.futures
import random
from queues import SmartQ
from icecream import ic

class ArtifactRunQArbEx(threading.Thread):
    _max_timeout = 0
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''
    _wait_queue = None
    _run_queue = None
    _done_queue = None
    _name = ''

    def __init__(self, config, system_config):
        super().__init__()
        self.config = config
        self.lock = threading.Lock()

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

            if not (self._wait_queue and self._run_queue and self._done_queue):
                raise ValueError("Queues not properly set up")

            while not self.config.test_eot:
                size = self._run_queue.qsize()
                if size < self.get_max_concurrent_task():
                    if not self._wait_queue.empty():
                        self.process_task()
                else:
                    if self._run_queue.empty() and self._wait_queue.empty() and not self._done_queue.empty():
                        self.config.test_eot = True

        except ValueError as ArtifactRunQArbEx_error:
            print(f"{self._name}:: Error in ArtifactRunQArbEx: {ArtifactRunQArbEx_error}")
            os._exit(1)

    def process_task(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            task = self._wait_queue.peek(release=False, acquire=True)
            if 'command' in task:
                run_command = task['command']
            else:
                raise ValueError("wait queue does not contain a 'command' key")

            task = self._wait_queue.get(release=False, acquire=False)
            subdir = os.path.join(self.config.root_dir, task['subdir'])
            for compile_task in list(self.config.compile_done_queue.queue):
                if '/'.join(compile_task['subdir'].split('/')[:2]) == '/'.join(task['subdir'].split('/')[:2]):
                    os.makedirs(subdir, exist_ok=True)
                    build_dir = os.path.join(self.config.root_dir, compile_task['subdir'])
                    if os.path.exists(build_dir):
                        shutil.copytree(build_dir, subdir, dirs_exist_ok=True)
                        future = executor.submit(subprocess.run, run_command.split(), cwd=subdir)
                        task['status'] = 'run'
                        task['future'] = future
                        self._run_queue.put(task,release=False, acquire=False)
            self._wait_queue.release()
