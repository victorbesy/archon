#pylint: disable=missing-class-docstring
#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=unused-import
#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=unused-argument

import concurrent.futures
import os
import threading
import queue
import datetime
import time
import shutil
import subprocess
import sys
import random
import toml
from pyee import EventEmitter
from icecream import ic

# Lock for updating seen_messages safely
seen_lock = threading.Lock()

class SmartQ(queue.Queue):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def peek(self):
        with self.lock:
            return self.queue[0] if not self.empty() else None

    def remove(self, element):
        # Create a temporary queue to hold elements
        with self.lock:
            temp_queue = queue.Queue()

            # Process each element in the original queue
            while not self.empty():
                current = self.get()
                # If the current element is not the one to remove, put it in the temporary queue
                if current != element:
                    temp_queue.put(current)
            # Restore the elements from the temporary queue back to the original queue
            while not temp_queue.empty():
                self.put(temp_queue.get())

    def confirm_read_and_maybe_remove(self, reader):
        with self.lock:
            if not self.empty():
                message = self.queue[0]
                message['status'][reader] = True
                if all(message['status'].values()):
                    self.get()  # Remove message once all have read it

    def iter_queue(self):
        """Return an iterator for the queue without removing items.
        for item in smart_queue.iter_queue():
        print(item)  # This prints each item without removing them from the queue
        """
        with self.lock:
            # Create a snapshot of the queue to iterate over
            snapshot = list(self.queue)
        for item in snapshot:
            yield item

    def iter_conditional(self, condition):
        """
        Iterates through the queue without removing items.
        Stops iteration if the condition is met.
        :param condition: A callable that takes an item from the queue and returns True to stop iteration.

        # Define a stopping condition function
        def stop_condition(item):
        # For example, stop when a message with a specific 'type' is encountered
        return item.get('type') == 'STOP'

        # Create an instance of SmartQ and populate it with some items
        smart_queue = SmartQ()
        # ... code to populate the queue ...

        # Use iter_conditional to iterate over items until the stop condition is met
        for item in smart_queue.iter_conditional(stop_condition):
        print(item)
        # Process the item...
        """
        with self.lock:
            # Iterate through a snapshot of the queue to safely check items without altering the queue
            for item in list(self.queue):
                yield item  # Yield the current item for processing
                if condition(item):  # Check the condition
                    break  # Exit the loop if condition is met

class BroadcastEvent:

    def __init__(self, ev_instruction, sender, receiver,QMessage):
        self.ev_instruction = ev_instruction  # The command of the event (e.g., "run thread")
        self.sender = sender  # Who sends the event
        self.receiver = receiver  # Intended receiver
        self.QMessage = QMessage # queue entry
        self._id = random.randint(1, 500000)  # Unique ID for the message

    def print_event(self,header=''):
        print(f" {header}:: Event: {self._id} {self.ev_instruction}, Sender: {self.sender}, Receiver: {self.receiver}, Message : {self.QMessage}")

    def get_id(self):
        return self._id
class EventUtils:

    EvEm = EventEmitter()

    def __init__(self,config):
        self.return_event = None
        self.events = []
        self.processed_event_ids = set()
        self.lock = threading.Lock()
        self.config = config

    # Implementing method to generate random events
    def generate_event(self,sender,receiver,Q_message,ev_instruction):
        with self.lock:
            #instructions = ["NOP","stop thread", "run thread", "wait for the next message", "exit thread"]
            event = BroadcastEvent(ev_instruction, sender, receiver,Q_message)
            #event.print_event("GENERATE:"+sender)
            self.events.append(event)
            self.EvEm.emit('broadcast_event', event)

    # Implementing method to listen events
    def listen_to_events(self,name):
        with self.lock:
            @self.EvEm.on('broadcast_event')
            def handle_event(event):
                unique_event_key = (event.get_id(), name)
                if event.sender == name:
                    return
                if unique_event_key in self.processed_event_ids:
                    return # Exit if this event has already been processed

                if event.receiver in("ALL", name) :
                    self.return_event = event
                    self.processed_event_ids.add(unique_event_key)  # Mark the event _id as processed
                    #event.print_event("LISTEN:"+name)
                    # Custom logic to handle different instructions
                    if event.ev_instruction == "exit thread":
                        self.config.compile_eot = True  # Example of handling an "exit thread" event
                        self.config.test_eot = True  # Example of handling an "exit thread" event
                return

class Config:
    compile_eot =False
    test_eot = False

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
                                         'approved': ['CompRunQMng'],
                                         'future':''})
        for command in run_commands['commands']:
            self.test_wait_queue.put({'command': command['command'],
                                      'subdir': command['subdir'],
                                      'status': '',
                                      'approved': [],
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

    def find_list_entry_index(self,in_list, target_entry):
        for index, entry in enumerate(in_list):
            if entry == target_entry:
                return index
        return None  # Return None if the entry is not found

    def remove_list_entry_by_index(self,in_list,index):
        if 0 <= index < len(in_list):
            del in_list[index]
            return in_list
        else:
            return False

class Watchdog(threading.Thread):
    def __init__(self, config, system_config):
        super().__init__()
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self._max_timeout = 0
        self._eot = False
        self._eot_mode = ''
        self._start = 1
        self._name = ''
        self.config = config
        self.event = EventUtils(config)

    def set_start(self,start):
        self._start = start

    def get_start(self):
        return self._start

    def set_eot_mode(self,eot_mode):
        if eot_mode in ['compile', 'run']:
            self._eot_mode = eot_mode
        else:
            raise ValueError("Invalid mode set. Choose either 'compile' or 'test'.")

    def get_eot_mode(self):
        return self._eot_mode

    def update_eot(self):
        if self._eot_mode == 'compile':
            self._eot = self.config.compile_eot
        elif self._eot_mode == 'run':
            self._eot = self.config.test_eot
        else:
            raise ValueError("Mode is not set. Cannot update EOT.")
        return self._eot

    def set_max_timeout(self, max_timeout):
        self._max_timeout = max_timeout

    def get_max_timeout(self):
        return self._max_timeout

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    # Getters
    def get_wait_queue(self):
        return self._wait_queue

    def get_run_queue(self):
        return self._run_queue

    def get_done_queue(self):
        return self._done_queue

    # Setters
    def set_wait_queue(self, q):
        if isinstance(q, SmartQ):
            self._wait_queue = q

    def set_run_queue(self, q):
        if isinstance(q, SmartQ):
            self._run_queue = q

    def set_done_queue(self, q):
        if isinstance(q, SmartQ):
            self._done_queue = q

    def run(self):

        if self._max_timeout <= 0:
            raise ValueError("Missing a corresponding max_timeout in script section of system_config")
        start_time = time.time()
        max_timeout = self.get_max_timeout()

        while  time.time() - start_time < max_timeout and self.update_eot() is False:

            self.event.listen_to_events(self._name)  # Start listening to events
            if self.event.return_event is not None:
                #self.event.return_event.print_event("DEBUG:"+self._name)
                self.event.return_event = None
            time.sleep(1)  # Check every second
            if self._start == 0 :
                max_timeout += 1

        if self._eot is False:
            for item in self._run_queue.queue:
                item['status'] = 'script_timeout'
            print(f"{self._name} :: Timeout reached {self.get_max_timeout()} sec. queues status:")
            self.config.print_queue(self._wait_queue, "wait")
            self.config.print_queue(self._run_queue, "run")
            self.config.print_queue(self._done_queue, "done")
            current_threads = threading.enumerate()
            for thread in current_threads:
                print(f"Thread name: {thread.name}")
            os._exit(1)  # Exit the entire script

class CompDoneQArbEx(threading.Thread):
    def __init__(self, config, system_config):
        super().__init__()
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self.config = config
        self.event = EventUtils(config)
        self.lock = threading.Lock()

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    # Getters
    def get_wait_queue(self):
        return self._wait_queue

    def get_run_queue(self):
        return self._run_queue

    def get_done_queue(self):
        return self._done_queue

    # Setters
    def set_wait_queue(self, q):
        if isinstance(q, SmartQ):
            self._wait_queue = q

    def set_run_queue(self, q):
        if isinstance(q, SmartQ):
            self._run_queue = q

    def set_done_queue(self, q):
        if isinstance(q, SmartQ):
            self._done_queue = q

    def run(self):
        empty_flag = True
        while self.config.compile_eot is False:
            with self.lock:
                self.event.listen_to_events(self._name)  # Start listening to events
                if self.event.return_event is not None:
                    #self.event.return_event.print_event("DEBUG:"+self._name)
                    self.event.return_event = None
            # Set up check for empty flag
            if empty_flag:
                # Check if _run_queue is empty
                if self._run_queue.empty():
                    # If it's empty, wait 1 sec and go back to the beginning of the loop
                    time.sleep(1)
                    continue
                else:
                    # Peek the current first entry from _run_queue
                    current_entry = self._run_queue.peek()
                    if current_entry is not None:
                        # Print future status
                        #print(f"Future status: {current_entry['future']._state} , return_code: {current_entry['future']._result.returncode}")

                        # Check if future is done
                        result  = current_entry['future'].result()
                        ic(result)
                        #if current_entry['future']._state == 'FINISHED':
                        # Move current_entry to the _done_queue
                        if current_entry['future'].result() == 0:
                            current_entry['status'] = 'ok'
                        else:
                            current_entry['status'] = 'error'
                        self._run_queue.remove(current_entry)
                        #if current_entry['future'].result() is not None:
                        #    print(f"Future status: {current_entry['future']._state} , return_code: {current_entry['future']._result.returncode}")
                        receiver = 'ALL'
                        with self.lock:
                            self._done_queue.put(current_entry)
                            self.event.generate_event(self._name,receiver,current_entry,"NOP")
                            # Reset check for empty flag
                            #self.empty_flag = False

class ArtifactDoneQMg(CompDoneQArbEx) :
    #def __init__(self, config, system_config):
    #    super().__init__(config, system_config)

    def run(self):
        empty_flag = True
        while self.config.test_eot is False:
            with self.lock:
                self.event.listen_to_events(self._name)  # Start listening to events
                if self.event.return_event is not None:
                    #self.event.return_event.print_event("DEBUG:"+self._name)
                    self.event.return_event = None
            # Set up check for empty flag
            if empty_flag:
                # Check if _run_queue is empty
                if self._run_queue.empty():
                    # If it's empty, wait 1 sec and go back to the beginning of the loop
                    time.sleep(1)
                    continue
                else:
                    # Peek the current first entry from _run_queue
                    current_entry = self._run_queue.peek()
                    #ic(current_entry)
                    if current_entry is not None:
                        # Print future status
                        #print(f"Future status: {current_entry['future']._state} , return_code: {current_entry['future']._result.returncode}")

                        # Check if future is done
                        #if current_entry['future']._state == 'FINISHED':
                        # Move current_entry to the _done_queue
                        if current_entry['future'].result() == 0:
                            current_entry['status'] = 'ok'
                        else:
                            current_entry['status'] = 'error'
                        self._run_queue.remove(current_entry)

                        #if current_entry['future'].result() is not None:
                        #    print(f"Future status: {current_entry['future']._state} , return_code: {current_entry['future']._result.returncode}")
                        receiver = 'ALL'
                        with self.lock:
                            self._done_queue.put(current_entry)
                            self.event.generate_event(self._name,receiver,current_entry,"NOP")
                            # Reset check for empty flag
                            #empty_flag = False

class CompRunQArbEx(threading.Thread):
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
        self.timeout_triggered = False
        self.event = EventUtils(config)
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
            #timeout_thread = threading.Thread(target=self.timeout_monitor)
            #timeout_thread.start()

            #if self._max_timeout <= 0:
            #    raise ValueError("Missing a corresponding max_timeout in script section of system_config")
            if not self._makefile_path:
                raise ValueError("Missing a corresponding makefile path in script section of system_config")

            if not (self._wait_queue and self._run_queue and self._done_queue):
                raise ValueError("Queues not set up properly")

            while self.config.compile_eot  is  False:
                self.event.listen_to_events(self._name)  # Start listening to events
                if self.event.return_event is not None:
                    #self.event.return_event.print_event("DEBUG:"+self._name)
                    self.event.return_event = None
                size= self._run_queue.qsize()
                if size < self.get_max_concurrent_task():
                    if not self._wait_queue.empty():
                        self.process_task()
                else:
                    time.sleep(1)  # Wait before checking the queue again
                if self._run_queue.empty() and self._wait_queue.empty() and not self._done_queue.empty():
                    self.config.compile_eot = True

        except ValueError as CompRunQArbEx_error:
            print(f"{self._name}:: Error in CompRunQArbEx: {CompRunQArbEx_error}")
            os._exit(1)

    def process_task(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:

            task = self._wait_queue.peek()
            if 'command' in task:
                run_command = task['command']  # This should be a list e.g., ["make", "-C", subdir]
            else:
                raise ValueError("wait queue does not contain a 'command' key")
            if 'approved' in task:
                approved = task['approved']
            else:
                raise ValueError("wait queue does not contain a 'approved' key")
            if len(approved) == 0 :
                task = self._wait_queue.get()
                subdir = os.path.join(self.config.root_dir, task['subdir'])
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


class ArtifactRunQArbEx(CompRunQArbEx):

    #def __init__(self, config, system_config):
    #    super().__init__(config, system_config)

    def run(self):
        try:
            if not self._makefile_path:
                raise ValueError("Missing a corresponding makefile path in script section of system_config")

            if not (self._wait_queue and self._run_queue and self._done_queue):
                raise ValueError("Queues not set up properly")

            while self.config.test_eot  is  False:
                self.event.listen_to_events(self._name)  # Start listening to events
                if self.event.return_event is not None:
                    #self.event.return_event.print_event("DEBUG:"+self._name)
                    self.event.return_event = None
                    #self.config.test_eot = True

                size= self._run_queue.qsize()
                if size < self.get_max_concurrent_task():
                    if not self._wait_queue.empty():
                        self.process_task()
                else:
                    time.sleep(1)  # Wait before checking the queue again
                if self._run_queue.empty() and self._wait_queue.empty() and not self._done_queue.empty():
                    self.config.test_eot = True


        except ValueError as ArtifactRunQArbEx_err:
            print(f"{self._name}:: Error in ArtifactRunQArbEx: {ArtifactRunQArbEx_err}")
            os._exit(1)


    def process_task(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            if not self.config.compile_done_queue.empty():
                task = self._wait_queue.get()
                if 'command' in task:
                    run_command = task['command']  # This should be a list e.g., ["make", "-C", subdir]
                else:
                    raise ValueError("wait queue does not contain a 'command' key")

                if 'approved' in task:
                    approved = task['approved']
                else:
                    raise ValueError("wait queue does not contain a 'approved' key")

                if len(approved) == 0 :
                    subdir = os.path.join(self.config.root_dir, task['subdir'])
                    for compile_task in list(self.config.compile_done_queue.queue):
                        if '/'.join(compile_task['subdir'].split('/')[:2]) == '/'.join(task['subdir'].split('/')[:2]):
                            os.makedirs(subdir, exist_ok=True)
                            build_dir = os.path.join(self.config.root_dir, compile_task['subdir'])
                            if os.path.exists(build_dir):
                                shutil.copytree(build_dir, subdir, dirs_exist_ok=True)
                                #ic(run_command)
                                # Execute the makefile (example: subprocess call)
                                future = executor.submit(subprocess.run, run_command.split(), cwd=subdir)
                                task['status'] = 'run'
                                task['future'] =  future
                                self._run_queue.put(task)
                            else : self._wait_queue.put(task)

class RunQMng(CompDoneQArbEx) :
    #def __init__(self, config, system_config):
    #    super().__init__(config, system_config)

    def run(self):
        while self.config.test_eot is False:
            with self.lock:
                self.event.listen_to_events(self._name)  # Start listening to events
                if self.event.return_event is not None:
                    #self.event.return_event.print_event("DEBUG:"+self._name)
                    self.event.return_event = None
                # Check if _wait_queue is empty
                if self._wait_queue.empty():
                    continue
                else:
                    self.process_runQ()
            time.sleep(1)

    def process_runQ(self):
        task = self._wait_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            task = self._wait_queue.get()
            task['approved']= self.config.remove_list_entry_by_index(task['approved'],hit)
            self._wait_queue.put(task)
        #ic()
#---\/---
#---/\---
class RuntimeTestMonitor(threading.Thread):
    # Implementation of RuntimeTestMonitor
    pass

class RuntimeMgr(threading.Thread):
    # Implementation of RuntimeMgr
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

        config = Config(regression_config)
        config.fill_queues(compile_commands, run_commands)
        config.set_status_wait(config.compile_wait_queue)
        config.set_status_wait(config.test_wait_queue)

        CompRunQArbEx_obj = CompRunQArbEx(config, system_config)
        CompRunQArbEx_obj.set_makefile_path(system_config['script']['compile_makefile'])
        CompRunQArbEx_obj.set_max_concurrent_task(system_config['script']['concurrent_compile'])
        CompRunQArbEx_obj.set_wait_queue(config.compile_wait_queue)
        CompRunQArbEx_obj.set_run_queue(config.compile_run_queue)
        CompRunQArbEx_obj.set_done_queue(config.compile_done_queue)
        CompRunQArbEx_obj.set_name("CompRunQArbEx")

        CompDoneQArbEx_obj = CompDoneQArbEx(config, system_config)
        CompDoneQArbEx_obj.set_wait_queue(config.compile_wait_queue)
        CompDoneQArbEx_obj.set_run_queue(config.compile_run_queue)
        CompDoneQArbEx_obj.set_done_queue(config.compile_done_queue)
        CompDoneQArbEx_obj.set_name("CompDoneQArbEx")

        CompRunQMng_obj = RunQMng(config, system_config)
        CompRunQMng_obj.set_wait_queue(config.compile_wait_queue)
        CompRunQMng_obj.set_run_queue(config.compile_run_queue)
        CompRunQMng_obj.set_done_queue(config.compile_done_queue)
        CompRunQMng_obj.set_name("CompRunQMng")

        CompWatchdog_obj = Watchdog (config, system_config)
        CompWatchdog_obj.set_wait_queue(config.compile_wait_queue)
        CompWatchdog_obj.set_run_queue(config.compile_run_queue)
        CompWatchdog_obj.set_done_queue(config.compile_done_queue)
        CompWatchdog_obj.set_name("CompWatchdog")
        CompWatchdog_obj.set_max_timeout(system_config['script']['max_timeout_compile'])
        CompWatchdog_obj.set_eot_mode('compile')

        ArtifactWatchdog_obj = Watchdog (config, system_config)
        ArtifactWatchdog_obj.set_wait_queue(config.test_wait_queue)
        ArtifactWatchdog_obj.set_run_queue(config.test_run_queue)
        ArtifactWatchdog_obj.set_done_queue(config.test_done_queue)
        ArtifactWatchdog_obj.set_name("ArtifactWatchdog")
        ArtifactWatchdog_obj.set_max_timeout(system_config['script']['max_timeout_test'])
        ArtifactWatchdog_obj.set_eot_mode('run')

        ArtifactRunQArbEx_obj = ArtifactRunQArbEx(config, system_config)
        ArtifactRunQArbEx_obj.set_makefile_path(system_config['script']['test_makefile'])
        ArtifactRunQArbEx_obj.set_max_concurrent_task(system_config['script']['concurrent_run'])
        ArtifactRunQArbEx_obj.set_wait_queue(config.test_wait_queue)
        ArtifactRunQArbEx_obj.set_run_queue(config.test_run_queue)
        ArtifactRunQArbEx_obj.set_done_queue(config.test_done_queue)
        ArtifactRunQArbEx_obj.set_name("ArtifactRunQArbEx")

        ArtifactDoneQArbEx_obj = ArtifactDoneQMg(config, system_config)
        ArtifactDoneQArbEx_obj.set_wait_queue(config.test_wait_queue)
        ArtifactDoneQArbEx_obj.set_run_queue(config.test_run_queue)
        ArtifactDoneQArbEx_obj.set_done_queue(config.test_done_queue)
        ArtifactDoneQArbEx_obj.set_name("ArtifactDoneQArbEx")

        #ArtifactRunQMng_obj = RunQMng(config, system_config)
        #ArtifactRunQMng_obj.set_wait_queue(config.test_wait_queue)
        #ArtifactRunQMng_obj.set_run_queue(config.tes_run_queue)
        #ArtifactRunQMng_obj.set_done_queue(config.test_done_queue)
        #ArtifactRunQMng_obj.set_name("CompRunQMng")


        threads = [
            CompDoneQArbEx_obj,
            CompRunQArbEx_obj,
            CompRunQMng_obj,
            CompWatchdog_obj,
            ArtifactWatchdog_obj,
            ArtifactRunQArbEx_obj,
            ArtifactDoneQArbEx_obj
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


        print("Graceful Shutdown:")
        config.print_queue(config.compile_wait_queue, "Compile Wait")
        config.print_queue(config.compile_run_queue, "Compile Run")
        config.print_queue(config.compile_done_queue, "Compile Done")
        config.print_queue(config.test_wait_queue, "Artifact Wait")
        config.print_queue(config.test_run_queue, "Artifact Run")
        config.print_queue(config.test_done_queue, "Artifact Done")
        # Optionally print the contents of other queues

    except ValueError as main_error:
        print(f"Error occurred in main: {main_error}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        args = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
        main(args["-regression_config"], args["-system_config"],
             "CompileCommands.toml", "RunCommands.toml")
    except ValueError as e:
        print(f"Error occurred: {e}")
        os._exit(1)
