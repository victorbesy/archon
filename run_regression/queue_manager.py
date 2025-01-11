
# queue_manager.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
from icecream  import ic
import time
import random

class QManager(threading.Thread) :
    _max_timeout = 0
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''
    _wait_queue = None
    _run_queue = None
    _done_queue = None
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
        while not self.force_to_exit_ev.is_set():
            if not self._wait_queue.is_empty():
                self.process_waitQ()
            if not self._run_queue.is_empty():
                self.process_runQ()
            if not self._done_queue.is_empty():
                self.process_doneQ()
            delay = random.uniform(0, 1)
            time.sleep(delay)

    def process_waitQ(self):
        task = self._wait_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            #get send  task to adviser
            self.config.comp_adv_req_queue.put(task)
            task1 = self.config.comp_adv_resp_queue.get()
            if task1 is not None:
                ic(task1)
            self._wait_queue.print_queue('QM')
            task['approved']= self.config.remove_list_entry_by_index(task['approved'],hit)
            self._wait_queue.print_queue('QM')
        else:
            task = self._wait_queue.rotate_left()

    def process_runQ(self):
        task = self._run_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            self._run_queue.print_queue('QM')
            #task['approved']= self.config.remove_list_entry_by_index(task['approved'],hit)
            self._run_queue.print_queue('QM')
    def process_doneQ(self):
        task = self._done_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            self._done_queue.print_queue('QM')
            #task['approved']= self.config.remove_list_entry_by_index(task['approved'],hit)
            self._done_queue.print_queue('QM')
