
# queue_manager.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
from icecream import ic
import time
import random
import threading

class SmartQUtils:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.adviser_response_dict = {
            "worker_execution": [
                "wait",
                "start",
                #"stop",
                #"pause",
                #"resume",
                #"restart",
                #"kill",
                #"finish",
                #"timeout",
                "NA"
            ],
            "get_worker_info": [
                "get log",
                "get status",
                "update state",
                "NA"
            ],
            "worker_resource_config": [
                "get config",
                "scale up memory",
                "scale down memory",
                "scale up cpu",
                "scale down cpu",
                "NA"
            ],
            "change_worker": [
                "update code",
                "deploy version",
                "rollback version",
                "NA"
            ]
        }
    def set_waitq_start_time(self, item, time_value):
        item['process_info']['waitq_start_time'] = time_value
        ic()

    def get_waitq_start_time(self, item):
        return item['process_info']['waitq_start_time']

    def set_runq_start_time(self, item, time_value):
        item['process_info']['runq_start_time'] = time_value
        
    def get_runq_start_time(self, item):
        return item['process_info']['runq_start_time']
    
    def set_doneq_start_time(self, item, time_value):
        item['process_info']['doneq_start_time'] = time_value
        
    def get_doneq_start_time(self, item):
        return item['process_info']['doneq_start_time']
    
    '''
    def set_adviser(self, item, adviser):
        item['adviser'][0] = adviser

    def get_adviser(self, item):
        return item['adviser'][0] if item['adviser'] else ''
    '''
     
    def set_adviser_resp(self, item, adviser,adviser_key='worker_execution'):
        item['adviser_response'][adviser_key] = adviser
        if self.verbose:
            print(f"Adviser set to {adviser} for item in {self._name} queue")

    def get_adviser_resp(self, item,adviser_key='worker_execution'):
        adviser = item['adviser_response'][adviser_key] if item['adviser_response'] else False
        if self.verbose:
            print(f"Adviser of item in {self._name} queue: {adviser}")
        return adviser
    
    def set_status(self, item, status):
        item['status'][0] = status

    def get_status(self, item):
        return item['status'][0] if item['status'] else ''

    def set_approved(self, item, approved):
        item['approved'][0] = approved

    def get_approved(self, item):
        return item['approved'][0] if item['approved'] else ''

    def compare(self, item1, item2):
        result = item1['command'] == item2['command'] and item1['subdir'] == item2['subdir']
        if self.verbose:
            if result:
                print(f"Items {item1} and {item2} are equal in 'command' and 'subdir'")
            else:
                print(f"Items {item1} and {item2} are not equal in 'command' and 'subdir'")

        return result
    