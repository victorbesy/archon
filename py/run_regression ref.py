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

class CompilationSupervisor(threading.Thread):

    def __init__(self, init, system_config):
        super().__init__()
        self.init = init
        self.concurrent_compile_counter = 0
        script_config = system_config.get('script', {})
        self.max_timeout_compile = script_config.get('max_timeout_compile', 0)
        self.compile_makefile = script_config.get('compile_makefile', '')
        self.max_concurrent_compile = script_config.get('concurrent_compile', 0) 

        if self.max_timeout_compile <=0  or not self.compile_makefile:
            raise ValueError("Missing max_timeout_compile or compile_makefile in script section of system_config")
     
        self.timeout_triggered = False
    
    def run(self):
        timeout_thread = threading.Thread(target=self.timeout_monitor)
        timeout_thread.start()

        while True:
            if self.concurrent_compile_counter < self.max_concurrent_compile:
                # ... Rest of the code in the run method
                if not self.init.compile_wait_queue.empty():
                    self.process_compile_task()
            else:
                time.sleep(1)  # Wait before checking the queue again

            self.check_run_compile_queue()

    def timeout_monitor(self):
        start_time = time.time()
        while time.time() - start_time < self.max_timeout_compile:
            time.sleep(1)  # Check every second

        for item in self.init.compile_run_queue.queue:
            item['status'] = 'script_timeout'
        print("Timeout reached. Compile queues status: ")
        self.init.print_queue(self.init.compile_wait_queue, "wait")
        self.init.print_queue(self.init.compile_run_queue, "run")
        self.init.print_queue(self.init.compile_done_queue, "done")
        os._exit(1)  # Exit the entire script

    def process_compile_task(self):
        task = self.init.compile_wait_queue.get()
        subdir = os.path.join(self.init.root_dir, task['subdir'])
        os.makedirs(subdir, exist_ok=True)
        shutil.copy(self.compile_makefile, subdir)

        # Execute the makefile (example: subprocess call)
        subprocess.run(["make", "-C", subdir])

        task['status'] = 'run'
        self.init.compile_run_queue.put(task)
        self.concurrent_compile_counter += 1

    def check_run_compile_queue(self):
        temp_queue = queue.Queue()
        while not self.init.compile_run_queue.empty():
            task = self.init.compile_run_queue.get()
            if task['status'] == 'done':
                self.init.compile_done_queue.put(task)
                self.concurrent_compile_counter -= 1
            else:
                temp_queue.put(task)
        while not temp_queue.empty():
            self.init.compile_run_queue.put(temp_queue.get())

'''' OLD TODO
class CompilationSupervisor(threading.Thread):
   
    def __init__(self, init, system_config):
        super().__init__()
        self.init = init

        script_config = system_config.get('script', {})
        self.max_timeout_compile = script_config.get('max_timeout_compile', 0)
        self.compile_makefile = script_config.get('compile_makefile', '')
        self.concurrent_compile_counter = script_config.get('concurrent_compile', 0)  # Ensure this is correctly initialized

        if not self.max_timeout_compile or not self.compile_makefile:
            raise ValueError("Missing max_timeout_compile or compile_makefile in script section of system_config")
     
        self.timeout_triggered = False

    def run(self):
        timeout_thread = threading.Thread(target=self.timeout_timer)
        timeout_thread.start()

        while not self.timeout_triggered:
            if self.concurrent_compile_counter < self.concurrent_compile_counter:
                self.process_compile_queue()
            else:
                self.check_run_compile_queue()
        timeout_thread.join()

    def timeout_timer(self):
        timer = 0
        while timer < self.max_timeout_compile:
            if self.timeout_triggered:
                break
            time.sleep(1)
            timer += 1
        self.timeout_triggered = True
        with self.init.compile_run_queue.mutex:
            self.init.print_queue(self.init.compile_wait_queue, "Compile Wait")
            self.init.print_queue(self.init.compile_run_queue, "Compile Run")
            self.init.print_queue(self.init.compile_done_queue, "Compile Done")
            while not self.init.compile_run_queue.empty():
                item = self.init.compile_run_queue.get()
                item['status'] = 'script_timeout'
                self.init.compile_run_queue.task_done()

    def process_compile_queue(self):
        if not self.init.compile_wait_queue.empty():
            item = self.init.compile_wait_queue.get()
            subdir = os.path.join(self.init.root_dir, item['subdir'])
            os.makedirs(subdir, exist_ok=True)
            shutil.copy(self.compile_makefile, subdir)
            subprocess.run(['make', '-C', subdir])
            item['status'] = 'run'
            self.init.compile_run_queue.put(item)
            self.concurrent_compile_counter += 1

    def check_run_compile_queue(self):
        temp_queue = queue.Queue()
        while not self.init.compile_run_queue.empty():
            item = self.init.compile_run_queue.get()
            if item['status'] == 'done':
                self.init.compile_done_queue.put(item)
                self.concurrent_compile_counter -= 1
            else:
                temp_queue.put(item)
        while not temp_queue.empty():
            self.init.compile_run_queue.put(temp_queue.get())
'''

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

    # Create and start threads
    threads = [
        CompilationTestMonitor(),
        CompilationSupervisor(init, system_config),
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
