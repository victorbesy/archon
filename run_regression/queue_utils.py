
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
import threading

class SmartQUtils:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.method_logging = {
            'set_adviser': False,
            'set_status': False,
            'set_approved': False,
            'get_adviser': False,
            'get_status': False,
            'get_approved': False,
             'compare': False
        }

    def log(self, method_name, *args, return_value=None):
        log_enabled = self.method_logging.get(method_name, self.verbose)
        if log_enabled:
            print(f"Object: {getattr(self, '_name', 'Unknown')}, Method: {method_name}")
            print(f"Arguments: {args}")
            if return_value is not None:
                print(f"Returns/Sets: {return_value}")
            print("----------")

    def set_adviser(self, item, adviser):
        item['adviser'][0] = adviser
        #self.log('set_adviser', item, adviser, return_value=adviser)

    def set_status(self, item, status):
        item['status'][0] = status
        #self.log('set_status', item, status, return_value=status)

    def set_approved(self, item, approved):
        item['approved'][0] = approved
        #self.log('set_approved', item, approved, return_value=approved)

    def get_adviser(self, item):
        adviser = item['adviser'][0] if item['adviser'] else ''
        #self.log('get_adviser', item, return_value=adviser)
        return adviser

    def get_status(self, item):
        status = item['status'][0] if item['status'] else ''
        #self.log('get_status', item, return_value=status)
        return status

    def get_approved(self, item):
        approved = item['approved'][0] if item['approved'] else ''
        #self.log('get_approved', item, return_value=approved)
        return approved

    def compare(self, item1, item2):
        #self.log('compare', item1, item2)
        result = item1['command'] == item2['command'] and item1['subdir'] == item2['subdir']
        if self.verbose:
            if result:
                print(f"Items {item1} and {item2} are equal in 'command' and 'subdir'")
            else:
                print(f"Items {item1} and {item2} are not equal in 'command' and 'subdir'")
        #self.log('compare', return_value=result)
        return result
    