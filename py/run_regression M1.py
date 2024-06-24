import os
import threading
import queue
import datetime
import toml
import time
import shutil 
import subprocess

class Init:
    def __init__(self, regression_config):
        self.regression_name = regression_config.get('regression_name', 'default_regression_name')
        self.create_directory()
        self.compile_wait_queue = queue.Queue()
        self.compile_run_queue = queue.Queue()
        self.compile_done_queue = queue.Queue()
        self.test_wait_queue = queue.Queue()
        self.test_run_queue = queue.Queue()
        self.test_done_queue = queue.Queue()

    def create_directory(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.root_dir = f"{self.regression_name}_{timestamp}"
        os.makedirs(self.root_dir, exist_ok=True)

    def fill_queues(self, compile_commands, run_commands):
        for command in compile_commands['commands']:
            self.compile_wait_queue.put({'command': command['command'], 
                                         'subdir': command['subdir'], 
                                         'status': ''})
        for command in run_commands['commands']:
            self.test_wait_queue.put({'command': command['command'], 
                                      'subdir': command['subdir'], 
                                      'status': ''})

    def set_status_wait(self, q):
        temp_queue = queue.Queue()
        while not q.empty():
            item = q.get()
            item['status'] = 'wait'
            temp_queue.put(item)
        while not temp_queue.empty():
            q.put(temp_queue.get())

    def print_queue(self, q, name):
        if not q.empty():
            print(f"{name} queue:")
        temp_queue = queue.Queue()
        while not q.empty():
            item = q.get()
            print(item)
            temp_queue.put(item)
        while not temp_queue.empty():
            q.put(temp_queue.get())
        if q.empty():
            print(f"{name} queue: Empty")
# Define other classes for Compilation and Runtime threads
class CompilationTestMonitor(threading.Thread):
    pass

class RegressionSupervisor(threading.Thread):
    _max_timeout = 0
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''

    def __init__(self, init, system_config):
        super().__init__()
        self.init = init
        self.concurrent_task_counter = 0
        script_config = system_config.get('script', {})
        self.timeout_triggered = False

    # Getter and Setter for max_timeout_task
    def set_max_timeout(self, max_timeout):
        self._max_timeout = max_timeout

    def get_max_timeout(self):
        return self._max_timeout

    # Getter and Setter for compile_makefile
    def set_makefile_path(self, makefile_path):
        self._makefile_path = makefile_path

    def get_makefile_path(self):
        return self._makefile_path

    # Getter and Setter for max_concurrent_task
    def set_max_concurrent_task(self, max_concurrent_task):
        self._max_concurrent_task = max_concurrent_task

    def get_max_concurrent_task(self):
        return self._max_concurrent_task

    # Getter and Setter for compile_dir
    def set_dir_path(self, dir_path):
        self._dir_path = dir_path

    def get_dir_path(self):
        return self._dir_path

    def run(self):
        timeout_thread = threading.Thread(target=self.timeout_monitor)
        timeout_thread.start()
        if self._max_timeout <= 0 :
            raise ValueError("Missing a corresponding max_timeout in script section of system_config")
        if not self._makefile_path:
            raise ValueError("Missing a corresponding makefile path in script section of system_config")
        
        while True:
            if self.concurrent_task_counter < self.get_max_concurrent_task():
                # ... Rest of the code in the run method
                if not self.init.compile_wait_queue.empty():
                    self.process_task_task()
            else:
                time.sleep(1)  # Wait before checking the queue again

            self.check_run_task_queue()

    def timeout_monitor(self):
        start_time = time.time()
        while time.time() - start_time < self.get_max_timeout():
            time.sleep(1)  # Check every second

        for item in self.init.compile_run_queue.queue:
            item['status'] = 'script_timeout'
        print("Timeout reached. Compile queues status: ")
        self.init.print_queue(self.init.compile_wait_queue, "wait")
        self.init.print_queue(self.init.compile_run_queue, "run")
        self.init.print_queue(self.init.compile_done_queue, "done")
        os._exit(1)  # Exit the entire script

    def process_task_task(self):
        task = self.init.compile_wait_queue.get()
        subdir = os.path.join(self.init.root_dir, task['subdir'])
        os.makedirs(subdir, exist_ok=True)
        shutil.copy(self.get_makefile_path(), subdir)

        # Execute the makefile (example: subprocess call)
        subprocess.run(["make", "-C", subdir])

        task['status'] = 'run'
        self.init.compile_run_queue.put(task)
        self.concurrent_task_counter += 1

    def check_run_task_queue(self):
        temp_queue = queue.Queue()
        while not self.init.compile_run_queue.empty():
            task = self.init.compile_run_queue.get()
            if task['status'] == 'done':
                self.init.compile_done_queue.put(task)
                self.concurrent_task_counter -= 1
            else:
                temp_queue.put(task)
        while not temp_queue.empty():
            self.init.compile_run_queue.put(temp_queue.get())




class RuntimeTestMonitor(threading.Thread):
    pass

class RuntimeSupervisor(threading.Thread):
    pass

class RuntimeServer(threading.Thread):
    pass

def main(regression_config_file, system_config_file, compile_commands_file, run_commands_file):
    regression_config = toml.load(regression_config_file)
    system_config = toml.load(system_config_file)
    compile_commands = toml.load(compile_commands_file)
    run_commands = toml.load(run_commands_file)

    init = Init(regression_config)
    init.fill_queues(compile_commands, run_commands)

    # Set status to 'wait' for all elements in wait queues
    init.set_status_wait(init.compile_wait_queue)
    init.set_status_wait(init.test_wait_queue)
    
    CompilationSupervisor_inst = RegressionSupervisor(init, system_config)
    CompilationSupervisor_inst.set_max_timeout(system_config['script']['max_timeout_compile'])
    CompilationSupervisor_inst.set_makefile_path(system_config['script']['compile_makefile'])
    CompilationSupervisor_inst.set_max_concurrent_task(system_config['script']['concurrent_compile'])
    CompilationSupervisor_inst.set_dir_path('path/to/compile/directory')
    

        
    # Create and start threads
    threads = [
        CompilationTestMonitor(),
        CompilationSupervisor_inst,
        RuntimeTestMonitor(),
        RuntimeSupervisor(),
        RuntimeServer()
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Print the contents of all queues
    init.print_queue(init.compile_wait_queue, "Compile Wait")
    init.print_queue(init.compile_run_queue, "Compile Run")
    init.print_queue(init.compile_done_queue, "Compile Done")
    #init.print_queue(init.test_wait_queue, "Test Wait")
    #init.print_queue(init.test_run_queue, "Test Run")
    #init.print_queue(init.test_done_queue, "Test Done")

if __name__ == "__main__":
    import sys
    args = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
    main(args["-regression_config"], args["-system_config"], 
         "CompileCommands.toml", "RunCommands.toml")
