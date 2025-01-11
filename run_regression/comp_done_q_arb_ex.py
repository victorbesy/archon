# comp_run_q_arb_ex.py

import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
import time
import random
from icecream  import ic

class CompDoneQArbEx(threading.Thread):
    def __init__(self, config, system_config,set_completion_ev):
        super().__init__()
        self.config = config
        self.system_config = system_config
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self.set_completion_ev  = set_completion_ev

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
                self._wait_queue.print_queue(self._name)
                self._run_queue.print_queue(self._name)
                self._done_queue.print_queue(self._name)
                if current_entry is not None:
                    result = current_entry['future'].result()
                    if result.returncode == 0:
                        current_entry['status'] = 'ok'
                    else:
                        current_entry['status'] = 'error'
                    self._run_queue.remove(current_entry)
                    self._done_queue.put(current_entry)

            current_size = self._done_queue.get_size()
            compile_size = self.config.get_number_of_compile_workers()

            if current_size == compile_size:
                if self.set_completion_ev :
                    self.set_completion_ev.set()
                self.config.compile_eot = True
