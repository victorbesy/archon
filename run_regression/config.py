# config.py

import os
import datetime
from queues import SmartQ

class Config:
    compile_eot = False
    test_eot = False
    watchdog_eot = False
    def __init__(self, regression_config):
        self.regression_name = regression_config.get('regression_name', 'default_regression_name')
        self.create_directory()
        self.compile_wait_queue = SmartQ(verbose=False,name="compile_wait_queue")
        self.compile_run_queue = SmartQ(verbose=False,name="compile_run_queue")
        self.compile_done_queue = SmartQ(verbose=False,name="compile_done_queue")
        self.test_wait_queue = SmartQ(verbose=False,name="test_wait_queue")
        self.test_run_queue = SmartQ(verbose=False,name="test_run_queue")
        self.test_done_queue = SmartQ(verbose=False,name="test_done_queue")
        self.comp_adv_req_queue = SmartQ(verbose=False,name="comp_adv_req_queue")
        self.comp_adv_resp_queue = SmartQ(verbose=False,name="comp_adv_resp_queue")
        self.number_of_compile_workers = 0
        self.number_of_test_workers = 0
        self.adviser_response_dict = {
        "worker_execution": [
            "wait",
            "start",
            "stop",
            "pause",
            "resume",
            "restart",
            "kill",
            "finish",
            "timeout"
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


    def set_number_of_compile_workers(self,number):
        self.number_of_compile_workers = number
    def set_number_of_test_workers(self,number):
        self.number_of_test_workers = number
    def get_number_of_compile_workers(self):
        return self.number_of_compile_workers
    def get_number_of_test_workers(self):
        return self.number_of_test_workers
    def set_watchdog_eot(self):
        self.watchdog_eot = True

    def reset_watchdog_eot(self):
        self.watchdog_eot = False

    def create_directory(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.root_dir = f"{self.regression_name}_{timestamp}"
        os.makedirs(self.root_dir, exist_ok=True)

    def fill_queues(self, compile_commands, run_commands):
        for command in compile_commands['commands']:
            self.compile_wait_queue.put({
                'command': command['command'],
                'subdir': command['subdir'],
                'status': '',
                'approved': ['CompRunQMng'],
                'adviser': '',
                'process': ''
            })
        for command in run_commands['commands']:
            self.test_wait_queue.put({
                'command': command['command'],
                'subdir': command['subdir'],
                'status': '',
                'approved': ['ArtRunQMng'],
                'adviser': '',
                'process': ''
            })

    def set_status_wait(self, q):
        temp_queue = SmartQ()
        while not q.is_empty():
            item = q.get()
            item['status'] = 'wait'
            temp_queue.put(item)
        while not temp_queue.is_empty():
            q.put(temp_queue.get())

    def find_list_entry_index(self, in_list, target_entry):
        for index, entry in enumerate(in_list):
            if entry == target_entry:
                return index

    def remove_list_entry_by_index(self, in_list, index):
        if 0 <= index < len(in_list):
            del in_list[index]
            return in_list
        else:
            return False
