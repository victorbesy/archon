
# queue_adviser.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
from queue_utils import SmartQUtils
from icecream import ic
import time
import random

class QAdviser(threading.Thread, SmartQUtils):
    def __init__(self, config, system_config, set_completion_ev):
        # Initialize parent classes
        threading.Thread.__init__(self)  # Initialize threading.Thread
        SmartQUtils.__init__(self, verbose=False)  # Initialize SmartQUtils
        self._input_queue = None
        self._output_queue = None
        self._name = ''

    def __init__(self, config, system_config, force_to_exit_ev, verbose=False):
        super().__init__()
        self.config = config
        self.timeout_triggered = False
        self.force_to_exit_ev = force_to_exit_ev
        self.verbose = verbose
        self.advisor_response_dict = {
            "worker_execution": [
                "wait",
                "start"
                #"stop",
                #"pause",
                #"resume",
                #"restart",
                #"kill",
                #"finish",
                #"timeout"
            ],
            "get_worker_info": [
                "get log",
                "get status",
                "update state"
            ],
            "worker_resource_config": [
                "get config",
                "scale up memory",
                "scale down memory",
                "scale up cpu",
                "scale down cpu"
            ],
            "change_worker": [
                "update code",
                "deploy version",
                "rollback version"
            ]
        }

    def log(self, method_name, *args, return_value=None):
        if self.verbose:
            print(f"Object: {self._name}, Method: {method_name}")
            print(f"Arguments: {args}")
            if return_value is not None:
                print(f"Returns: {return_value}")
            print("----------")
    
    def set_name(self, name):
        self._name = name
        self.log("set_name", name)

    def get_name(self):
        return_value = self._name
        self.log("get_name", return_value=return_value)
        return return_value
    
    def set_input_queue(self, input_queue):
        self._input_queue = input_queue
        self.log("set_input_queue", input_queue)

    def get_input_queue(self):
        return_value = self._input_queue
        self.log("get_input_queue", return_value=return_value)
        return return_value
    
    def set_output_queue(self, output_queue):
        self._output_queue = output_queue
        self.log("set_output_queue", output_queue)

    def get_output_queue(self):
        return_value = self._output_queue
        self.log("get_output_queue", return_value=return_value)
        return return_value
    
    def run(self):
        self.log("run")
        while not self.force_to_exit_ev.is_set():
            if not self._input_queue.is_empty():
                self.process_inputQ()
            else:
                delay = random.uniform(0, 1)
                time.sleep(delay)

    def process_inputQ(self):
        task = self._input_queue.get()
        self.log("process_inputQ", task)
        advice = self.get_advisor_response_list("worker_execution")
        self._input_queue.set_adviser(task,advice)
        self._output_queue.put(task)
        
       

    def get_advisor_response_list(self, subsection=None):
        #print(advisor.get_advisor_response_list("worker_execution"))  # Random word from 'worker_execution'
        if subsection and subsection in self.advisor_response_dict:
            responses = self.advisor_response_dict[subsection]
        else:
            responses = [word for sublist in self.advisor_response_dict.values() for word in sublist]
        
        if not responses:
            return_value = None
        else:
            return_value = random.choice(responses)

        self.log("get_advisor_response_list", subsection, return_value=return_value)
        return return_value
