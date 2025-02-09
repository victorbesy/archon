
# queue_adviser.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
from icecream  import ic
import time
import random

class QAdviser(threading.Thread) :
    _input_queue = None
    _output_queue = None
    _name = ''

    def __init__(self, config,system_config,force_to_exit_ev):
        super().__init__()
        self.config = config
        self.timeout_triggered = False
        self.force_to_exit_ev=force_to_exit_ev

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_input_queue(self, input_queue):
        self._input_queue = input_queue

    def get_input_queue(self):
        return self._input_queue

    def set_output_queue(self, output_queue):
        self._output_queue = output_queue

    def get_output_queue(self):
        return self._output_queue
    
    def run(self):
        while not self.force_to_exit_ev.is_set():
            if not self._input_queue.is_empty():
                self.process_inputQ()
            else:
                delay = random.uniform(0, 1)
                time.sleep(delay)

    def process_inputQ(self):
        task = self._input_queue.get()
        #set output quueue TODO!!!
        #ic(task)
        #ic()
    
   
