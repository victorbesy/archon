import concurrent.futures
import os
import threading
import queue
import datetime
import toml
import time
import shutil
import subprocess
import sys
class SmartQ(queue.Queue):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
    
    def peek(self):
        with self.lock:
            return self.queue[0] if not self.empty() else None


class Init:
    def __init__(self, regression_config):
        self.regression_name = regression_config.get('regression_name', 'default_regression_name')
        self.create_directory()
        self.compile_wait_queue = SmartQ()
        self.compile_run_queue = SmartQ()
        self.compile_done_queue = SmartQ()
        self.test_wait_queue = SmartQ()
        self.test_run_queue = SmartQ()
        self.test_done_queue = SmartQ()

    def create_directory(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.root_dir = f"{self.regression_name}_{timestamp}"
        os.makedirs(self.root_dir, exist_ok=True)

    def fill_queues(self, compile_commands, run_commands):
        for command in compile_commands['commands']:
            self.compile_wait_queue.put({'command': command['command'], 
                                         'subdir': command['subdir'], 
                                         'status': '',
                                         'future':''})
        for command in run_commands['commands']:
            self.test_wait_queue.put({'command': command['command'], 
                                      'subdir': command['subdir'], 
                                      'status': '',
                                      'future':''
                                      })

    def set_status_wait(self, q):
        temp_queue = SmartQ()
        while not q.empty():
            item = q.get()
            item['status'] = 'wait'
            temp_queue.put(item)
        while not temp_queue.empty():
            q.put(temp_queue.get())

    def print_queue(self, q, name):
        if not q.empty():
            print(f"{name} queue:")
        else:
            print(f"{name} queue: Empty")

        temp_queue = SmartQ()
        while not q.empty():
            item = q.get()
            print(item)
            temp_queue.put(item)
    
        while not temp_queue.empty():
            q.put(temp_queue.get())
 

class CompilationTestMonitor(threading.Thread):
    # Implementation of CompilationTestMonitor
    pass

class RegressionSupervisor(threading.Thread):
    _max_timeout = 0
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''
    _wait_queue = None
    _run_queue = None
    _done_queue = None
    _name = ''
    
    def __init__(self, init, system_config):
        super().__init__()
        self.init = init
        self.concurrent_task_counter = 0
        script_config = system_config.get('script', {})
        self.timeout_triggered = False

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_max_timeout(self, max_timeout):
        self._max_timeout = max_timeout

    def get_max_timeout(self):
        return self._max_timeout

    def set_makefile_path(self, makefile_path):
        self._makefile_path = makefile_path

    def get_makefile_path(self):
        return self._makefile_path

    def set_max_concurrent_task(self, max_concurrent_task):
        self._max_concurrent_task = max_concurrent_task

    def get_max_concurrent_task(self):
        return self._max_concurrent_task

    def set_dir_path(self, dir_path):
        self._dir_path = dir_path

    def get_dir_path(self):
        return self._dir_path

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
            timeout_thread = threading.Thread(target=self.timeout_monitor)
            timeout_thread.start()

            if self._max_timeout <= 0:
                raise ValueError("Missing a corresponding max_timeout in script section of system_config")
            if not self._makefile_path:
                raise ValueError("Missing a corresponding makefile path in script section of system_config")

            if not (self._wait_queue and self._run_queue and self._done_queue):
                raise ValueError("Queues not set up properly")

            while True:
                if self.concurrent_task_counter < self.get_max_concurrent_task():
                    if not self._wait_queue.empty():
                        self.process_task()
                else:
                    time.sleep(1)  # Wait before checking the queue again

                self.check_run_task_queue()

        except ValueError as e:
            print(f"{self._name}:: Error in RegressionSupervisor: {e}")
            os._exit(1)

    def timeout_monitor(self):
        start_time = time.time()
        while time.time() - start_time < self.get_max_timeout():
            time.sleep(1)  # Check every second

        for item in self._run_queue.queue:
            item['status'] = 'script_timeout'
        print(f"{self._name} :: Timeout reached {self.get_max_timeout()} sec. queues status:")
        self.init.print_queue(self._wait_queue, "wait")
        self.init.print_queue(self._run_queue, "run")
        self.init.print_queue(self._done_queue, "done") 
        os._exit(1)  # Exit the entire script
    

    
    def process_task(self):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                task = self._wait_queue.get()
                if 'command' in task:
                    run_command = task['command']  # This should be a list e.g., ["make", "-C", subdir]
                else:
                    raise ValueError("wait queue does not contain a 'command' key")
    
                subdir = os.path.join(self.init.root_dir, task['subdir'])
                os.makedirs(subdir, exist_ok=True)
                
                # Assuming self.get_makefile_path() is defined elsewhere in your class
                makefile_path = self.get_makefile_path()

                # Check if the path is a directory
                if os.path.isdir(makefile_path):
                    # Copy all files in the directory
                    for filename in os.listdir(makefile_path):
                        full_file_path = os.path.join(makefile_path, filename)
                        if os.path.isfile(full_file_path):  # Ensure it's a file, not a directory
                         shutil.copy(full_file_path, subdir)
                else:
                    # Path is a file, so just copy the file
                    shutil.copy(makefile_path, subdir)
                    
                # Execute the makefile (example: subprocess call)
                future = executor.submit(subprocess.run, run_command.split(), cwd=subdir)

                task['status'] = 'run'
                task['future'] =  future
                self._run_queue.put(task)
                self.concurrent_task_counter += 1

    def check_run_task_queue(self):
        temp_queue = SmartQ()
        while not self._run_queue.empty():
            task = self._run_queue.get()
            if task['status'] == 'done':
                self._done_queue.put(task)
                self.concurrent_task_counter -= 1
            else:
                temp_queue.put(task)
        while not temp_queue.empty():
            self._run_queue.put(temp_queue.get())

class TaskRegressionSupervisor(RegressionSupervisor):
    
    def process_task(self):      
        if not self.init.compile_done_queue.empty():
            task = self._wait_queue.get()
            subdir = os.path.join(self.init.root_dir, task['subdir'])
            #print(f" DEBUG: {task}")
            for compile_task in list(self.init.compile_done_queue.queue):
                if '/'.join(compile_task['subdir'].split('/')[:2]) == '/'.join(task['subdir'].split('/')[:2]):
                    os.makedirs(subdir, exist_ok=True)
                    build_dir = os.path.join(self.init.root_dir, compile_task['subdir'])
                    if os.path.exists(build_dir):
                        shutil.copytree(build_dir, subdir, dirs_exist_ok=True)
                        subprocess.run(['make', '-C', subdir])
                        task['status'] = 'run'
                        self._run_queue.put(task)
                        self.concurrent_task_counter += 1
                else : self._wait_queue.put(task)
  
class RuntimeTestMonitor(threading.Thread):
    # Implementation of RuntimeTestMonitor
    pass

class RuntimeSupervisor(threading.Thread):
    # Implementation of RuntimeSupervisor
    pass

class RuntimeServer(threading.Thread):
    # Implementation of RuntimeServer
    pass

def main(regression_config_file, system_config_file, compile_commands_file, run_commands_file):
    try:
        regression_config = toml.load(regression_config_file)
        system_config = toml.load(system_config_file)
        compile_commands = toml.load(compile_commands_file)
        run_commands = toml.load(run_commands_file)

        init = Init(regression_config)
        init.fill_queues(compile_commands, run_commands)
        init.set_status_wait(init.compile_wait_queue)
        init.set_status_wait(init.test_wait_queue)
        
        CompilationSupervisor_obj = RegressionSupervisor(init, system_config)
        CompilationSupervisor_obj.set_max_timeout(system_config['script']['max_timeout_compile'])
        CompilationSupervisor_obj.set_makefile_path(system_config['script']['compile_makefile'])
        CompilationSupervisor_obj.set_max_concurrent_task(system_config['script']['concurrent_compile'])
        CompilationSupervisor_obj.set_wait_queue(init.compile_wait_queue)
        CompilationSupervisor_obj.set_run_queue(init.compile_run_queue)
        CompilationSupervisor_obj.set_done_queue(init.compile_done_queue)
        CompilationSupervisor_obj.set_name("CompilationSupervisor")
        
        RuntimeSupervisor_obj = TaskRegressionSupervisor(init, system_config)
        RuntimeSupervisor_obj.set_max_timeout(system_config['script']['max_timeout_run'])
        RuntimeSupervisor_obj.set_makefile_path(system_config['script']['run_makefile'])
        RuntimeSupervisor_obj.set_max_concurrent_task(system_config['script']['concurrent_run'])
        RuntimeSupervisor_obj.set_wait_queue(init.test_wait_queue)
        RuntimeSupervisor_obj.set_run_queue(init.test_run_queue)
        RuntimeSupervisor_obj.set_done_queue(init.test_done_queue)
        RuntimeSupervisor_obj.set_name("RunTimeSupervisor")

        threads = [
            CompilationTestMonitor(),
            CompilationSupervisor_obj,
            RuntimeTestMonitor(),
            RuntimeSupervisor_obj,
            RuntimeServer()
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        init.print_queue(init.compile_wait_queue, "Compile Wait")
        init.print_queue(init.compile_run_queue, "Compile Run")
        init.print_queue(init.compile_done_queue, "Compile Done")
        # Optionally print the contents of other queues

    except ValueError as e:
        print(f"Error occurred in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        args = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
        main(args["-regression_config"], args["-system_config"], 
             "CompileCommands.toml", "RunCommands.toml")
    except ValueError as e:
        print(f"Error occurred: {e}")
        os._exit(1)

