
# queue_manager.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
from queues import SmartQ
from icecream import ic
import time
import random

class QManager(threading.Thread):
    _max_timeout = 0
    _makefile_path = ''
    _max_concurrent_task = 0
    _dir_path = ''
    _wait_queue = None
    _run_queue = None
    _done_queue = None
    _name = ''

    def __init__(self, config, system_config, force_to_exit_ev, verbose=False):
        super().__init__()
        self.config = config
        self.timeout_triggered = False
        self.force_to_exit_ev = force_to_exit_ev
        self.verbose = verbose  # Added verbose parameter

        # Individual method logging controls
        self.method_logging = {
            'set_name': False,
            'get_name': False,
            'set_makefile_path': False,
            'get_makefile_path': False,
            'set_max_concurrent_task': False,
            'get_max_concurrent_task': False,
            'set_wait_queue': False,
            'get_wait_queue': False,
            'set_run_queue': False,
            'get_run_queue': False,
            'set_done_queue': False,
            'get_done_queue': False,
            'run': False,
            'process_waitQ': False,
            'process_advice': False,
            'get_advice': False,
            'process_runQ': False,
            'process_doneQ': False,
            'set_adviser': False,
            'set_status': False,
            'set_approved': False,
            'get_adviser': False,
            'get_status': False,
            'get_approved': False,
            'compare': False,
        }

    def log(self, method_name, *args, return_value=None):
        log_enabled = self.method_logging.get(method_name, self.verbose)
        if log_enabled:
            print(f"Object: {self._name}, Method: {method_name}")
            print(f"Arguments: {args}")
            if return_value is not None:
                print(f"Returns/Sets: {return_value}")
            print("----------")

    def set_name(self, name):
        self._name = name
        self.log('set_name', name, return_value=name)

    def get_name(self):
        result = self._name
        self.log('get_name', return_value=result)
        return result

    def set_makefile_path(self, makefile_path):
        self._makefile_path = makefile_path
        self.log('set_makefile_path', makefile_path, return_value=makefile_path)

    def get_makefile_path(self):
        result = self._makefile_path
        self.log('get_makefile_path', return_value=result)
        return result

    def set_max_concurrent_task(self, max_concurrent_task):
        self._max_concurrent_task = max_concurrent_task
        self.log('set_max_concurrent_task', max_concurrent_task, return_value=max_concurrent_task)

    def get_max_concurrent_task(self):
        result = self._max_concurrent_task
        self.log('get_max_concurrent_task', return_value=result)
        return result

    def set_wait_queue(self, wait_queue):
        self._wait_queue = wait_queue
        self.log('set_wait_queue', wait_queue, return_value=wait_queue)

    def get_wait_queue(self):
        result = self._wait_queue
        self.log('get_wait_queue', return_value=result)
        return result

    def set_run_queue(self, run_queue):
        self._run_queue = run_queue
        self.log('set_run_queue', run_queue, return_value=run_queue)

    def get_run_queue(self):
        result = self._run_queue
        self.log('get_run_queue', return_value=result)
        return result

    def set_done_queue(self, done_queue):
        self._done_queue = done_queue
        self.log('set_done_queue', done_queue, return_value=done_queue)

    def get_done_queue(self):
        result = self._done_queue
        self.log('get_done_queue', return_value=result)
        return result

    def run(self):
        self.log('run')
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
        self.log('process_waitQ')
        task = self._wait_queue.get()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            # Check task status
            status = self.get_status(task)
            self.log('process_waitQ', f"Status: {status}")
            match status:
                case 'wait':
                    self.config.comp_adv_req_queue.put(task)
                    self.set_status(task, 'wait_adv_resp')
                case 'wait_adv_resp':
                    if not self.config.comp_adv_resp_queue.is_empty():
                        responce_task = self.config.comp_adv_resp_queue.seek(task)
                        if responce_task != False:
                            self.set_status(responce_task, 'wait')
                            task_updated = self.process_advice(task, hit)
                            self.config.comp_adv_resp_queue.remove(responce_task)  
                            task = task_updated
            self._wait_queue.put(task)
        else:
            task = self._wait_queue.rotate_left()

    def process_advice(self, q_entry, q_entry_index):
        self.log('process_advice', q_entry, q_entry_index)
        advice = self.get_advice(q_entry)
        ic("process_advice",advice)
        self.log('process_advice', f"Advice: {advice}")
        match advice:
            case 'wait':
                self.set_status(q_entry, 'wait')
            case 'start':
                self.set_status(q_entry, 'execute')
                q_entry['approved'] = self.config.remove_list_entry_by_index(q_entry['approved'], q_entry_index)
                self.log('process_advice', f"Updated approved list: {q_entry['approved']}")
            # case 'finish':   TODO
            # case 'cancel':   TODO
            case _:
                self.set_status(q_entry, 'wait')
                ic("process_advice","case_", advice)
        self.log('process_advice', return_value=q_entry)
        return q_entry

    def get_advice(self, q_entry):
        self.log('get_advice', q_entry)
        result = False
        if not self.config.comp_adv_resp_queue.is_empty():
            resp = self.config.comp_adv_resp_queue.seek(q_entry)
            ic()
            ic("get_advice",resp)
            if resp != False:
                result = self.config.comp_adv_resp_queue.get_adviser(resp)
        self.log('get_advice', return_value=result)
        ic("get_advice",result)
        ic()
        return result

    def process_runQ(self):
        self.log('process_runQ')
        task = self._run_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            self._run_queue.print_queue('QM')
            # task['approved'] = self.config.remove_list_entry_by_index(task['approved'], hit)
            self._run_queue.print_queue('QM')

    def process_doneQ(self):
        self.log('process_doneQ')
        task = self._done_queue.peek()
        hit = self.config.find_list_entry_index(task['approved'], self._name)
        if hit is not None:
            self._done_queue.print_queue('QM')
            # task['approved'] = self.config.remove_list_entry_by_index(task['approved'], hit)
            self._done_queue.print_queue('QM')

    # Set methods

    def set_adviser(self, item, adviser):
        item['adviser'][0] = adviser
        self.log('set_adviser', item, adviser, return_value=adviser)

    def set_status(self, item, status):
        item['status'][0] = status
        self.log('set_status', item, status, return_value=status)

    def set_approved(self, item, approved):
        item['approved'][0] = approved
        self.log('set_approved', item, approved, return_value=approved)

    # Get methods

    def get_adviser(self, item):
        adviser = item['adviser'][0] if item['adviser'] else ''
        self.log('get_adviser', item, return_value=adviser)
        return adviser

    def get_status(self, item):
        status = item['status'][0] if item['status'] else ''
        self.log('get_status', item, return_value=status)
        return status

    def get_approved(self, item):
        approved = item['approved'][0] if item['approved'] else ''
        self.log('get_approved', item, return_value=approved)
        return approved

    def compare(self, item1, item2):
        self.log('compare', item1, item2)
        result = item1['command'] == item2['command'] and item1['subdir'] == item2['subdir']
        if self.verbose:
            if result:
                print(f"Items {item1} and {item2} are equal in 'command' and 'subdir'")
            else:
                print(f"Items {item1} and {item2} are not equal in 'command' and 'subdir'")
        self.log('compare', return_value=result)
        return result
