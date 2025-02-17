# comp_run_q_arb_ex.py

import os
import shutil
import subprocess
import threading
import concurrent.futures
import psutil
from queues import SmartQ
import time
import random
from icecream  import ic
from queue_utils import SmartQUtils
import time 
class CompDoneQArbEx(threading.Thread, SmartQUtils):
    def __init__(self, config, system_config,set_completion_ev):
        super().__init__()
        self.config = config
        self.system_config = system_config
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self.set_completion_ev  = set_completion_ev
        self.previous_process_info = {}
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

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
        while not self.config.compile_eot:
            if self._run_queue.is_empty():
                delay = random.uniform(0, 1)
                time.sleep(delay)
                continue
            else:
                current_entry = self._run_queue.peek()
                #self._wait_queue.print_queue(self._name)
                #self._run_queue.print_queue(self._name)
                #self._done_queue.print_queue(self._name)
                if current_entry is not None:
                    result = current_entry['process'].poll()
                    if result is not None:
                        returncode = current_entry['future'].result()
                        process = current_entry['process']
                        if returncode == 0:
                            current_entry['status'] = 'ok'
                        else:
                            current_entry['status'] = 'error'  
                        self.set_doneq_start_time(current_entry,time.time())
                        self._run_queue.remove(current_entry)
                        self._done_queue.put(current_entry)
                    else:
                        pid = current_entry['pid']
                        process_info =  self.get_process_info(pid) 
                        if process_info is not None:  
                            for key in current_entry['process_info']:
                                if key in process_info:
                                    current_entry['process_info'][key] = process_info[key]    
            current_size = self._done_queue.get_size()
            compile_size = self.config.get_number_of_compile_workers()

            if current_size == compile_size:
                if self.set_completion_ev :
                    self.set_completion_ev.set()
                self.config.compile_eot = True

    
    def get_process_info(self, pid):
        """Fetch and print process information safely."""
        try:
            if not psutil.pid_exists(pid):
                print(f"Process {pid} does not exist.")
                return None

            p = psutil.Process(pid)
            process_info = {
                "pid": pid,
                "memory_rss": p.memory_info().rss,  # Resident Set Size
                "memory_vms": p.memory_info().vms,  # Virtual Memory Size
                "memory_percent": p.memory_percent(),
                "cpu_percent": p.cpu_percent(interval=1.0),
                "cpu_times": p.cpu_times(),
                "cpu_num": p.cpu_num()
            }

            updated_info = {}
            previous_info = self.previous_process_info.get(pid, {})

            # Update process_info only if new element is greater than old one
            for key, value in process_info.items():
                if key in previous_info:
                    if value > previous_info[key]:
                        updated_info[key] = value
                    else:
                        updated_info[key] = previous_info[key]
                else:
                    updated_info[key] = value

            # Check if there's any difference between updated_info and previous_info
            if previous_info != updated_info:
                self.previous_process_info[pid] = updated_info
                print("Process Information has changed:")
                for key, value in updated_info.items():
                    print(f"{key}: {value}")
                return updated_info
            else:
                print(f"Process information for PID {pid} has not changed.")
                return None

        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist (NoSuchProcess).")
        except psutil.AccessDenied:
            print(f"Permission denied to access process {pid} (AccessDenied).")
        except psutil.ZombieProcess:
            print(f"Process {pid} is a zombie (ZombieProcess).")
        except Exception as e:
            print(f"Unexpected error accessing process {pid}: {e}")
        