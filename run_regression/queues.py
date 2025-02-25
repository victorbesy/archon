
import threading
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
import random
from functools import wraps
from queue_utils import SmartQUtils
import time
import csv
def lock_sync(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self.lock:
            return func(self, *args, **kwargs)
    return wrapper

class SmartQ(deque,SmartQUtils):
    def __init__(self, verbose=True, name="NA"):
        SmartQUtils.__init__(self, verbose=False)  # Initialize SmartQUtils
        deque.__init__(self)
        self.lock = threading.Lock()
        self.verbose = verbose
        self._name = name
        if self.verbose:
            print(f"{self._name} queue created")

    @lock_sync
    def get_size(self):
        size = len(self)
        if self.verbose:
            print(f"Size of {self._name} queue: {size}")
        return size

    
    @lock_sync
    def get_name(self):
        name = self._name
        if self.verbose:
            print(f"queue: {name}")
        return name
    
    @lock_sync
    def put(self, item):
        self.append(item)
        if self.verbose:
            print(f"Item {item} added to {self._name} queue")

    @lock_sync
    def get(self):
        if self:
            item = self.popleft()
            if self.verbose:
                print(f"Item {item} removed from {self._name} queue")
            return item
        if self.verbose:
            print(f"No item to remove from {self._name} queue")
        return None

    @lock_sync
    def peek(self):
        if self:
            item = self[0]
            if self.verbose:
                print(f"Peek item in {self._name} queue: {item}")
            return item
        if self.verbose:
            print(f"No item to peek in {self._name} queue")
        return None

    @lock_sync
    def remove(self, item):
        try:
            super().remove(item)
            if self.verbose:
                print(f"Item {item} removed from {self._name} queue")
            return 0
        except ValueError:
            if self.verbose:
                print(f"Item {item} not found in {self._name} queue")
            return -1

    @lock_sync
    def is_empty(self):
        empty = len(self) == 0
        if self.verbose:
            print(f"{self._name} queue is {'empty' if empty else 'not empty'}")
        return empty

    @lock_sync
    def rotate_left(self):
        super().rotate(-1)
        if self.verbose:
            print(f"{self._name} queue rotated one element to the left")

    @lock_sync
    def print_queue(self, prefix=""):
        if self:
            print(f"{prefix} {self._name} queue:")
            for item in self:
                print(item)
        else:
            print(f"{self._name} queue: Empty")
    
    def init_queue(self, commands):
        for command in commands['commands']:
            
            self.put({
                'command': command['command'],
                'subdir': command['subdir'],
                'status': '',
                'approved': '',
                'adviser': '',
                'process': '',
                'process_info':{
                    "pid": 0,
                    "memory_rss": 0,  # Resident Set Size
                    "memory_vms": 0,  # Virtual Memory Size
                    "memory_percent": 0,
                    "cpu_percent":0,
                    "cpu_times": {},
                    "cpu_num": 0,
                    "waitq_start_time": 0,
                    "runq_start_time": 0,
                    "doneq_start_time": 0
                },
                'adviser_response': {},
                'pid':0                
            })
            
        if self.verbose:
            print(f"{self._name} queue initialized with commands")

    @lock_sync    
    def set_queue_default(self, approved, status):
        for item in self:
            #item['adviser'] = [adviser]
            item['status'] = [status]
            item['approved'] = [approved]
            item['adviser_response'] = {key: 'NA' for key in self.adviser_response_dict.keys()}
            self.set_waitq_start_time(item, time.time())
        if self.verbose:
            print(f"adviser_response set to default, approved set to {approved}, and status set to {status} for all items in {self._name} queue")

    @lock_sync
    def set_status(self, item, status):
        item['status'] = status
        if self.verbose:
            print(f"Status set to {status} for item in {self._name} queue")

    @lock_sync
    def set_approved(self, item, approved):
        item['approved'] = approved
        if self.verbose:
            print(f"Approved set to {approved} for item in {self._name} queue")


    @lock_sync
    def get_status(self, item):
        status = item['status'] if item['status'] else ''
        if self.verbose:
            print(f"Status of item in {self._name} queue: {status}")
        return status

    @lock_sync
    def get_approved(self, item):
        approved = item['approved'] if item['approved'] else ''
        if self.verbose:
            print(f"Approved of item in {self._name} queue: {approved}")
        return approved

    @lock_sync
    def compare(self, item1, item2):
        if item1['command'] == item2['command'] and item1['subdir'] == item2['subdir']:
            if self.verbose:
                print(f"Items {item1} and {item2} are equal in terms of 'command' and 'subdir'")
            return True
        if self.verbose:
            print(f"Items {item1} and {item2} are not equal in terms of 'command' and 'subdir'")
        return False
    @lock_sync
    def seek(self, entry):
        for item in self:
            if item['command'] == entry['command'] and item['subdir'] == entry['subdir']:
                if self.verbose:
                    print(f"Found matching item in {self._name} queue: {item}")
                return item
        if self.verbose:
            print(f"No matching item found in {self._name} queue for entry: {entry}")
        return False
    @lock_sync    
    def visualize_schedule(self):
        fig, ax = plt.subplots(figsize=(10, len(self) * 0.5))

        y_positions = range(len(self))
        colors = {'waiting': 'orange', 'running': 'green'}
        total_time_spent = 0
        min_start_time = float('inf')
        max_end_time = float('-inf')

        for i, job in enumerate(self):
            process_info = job['process_info']
            wait_start = process_info['waitq_start_time']
            run_start = process_info['runq_start_time']
            done_time = process_info['doneq_start_time']

            wait_time = run_start - wait_start
            run_time = done_time - run_start
            total_time = done_time - wait_start

            min_start_time = min(min_start_time, wait_start)
            max_end_time = max(max_end_time, done_time)

            ax.broken_barh([(wait_start, wait_time)], (i - 0.3, 0.6), facecolors=colors['waiting'])
            ax.broken_barh([(run_start, run_time)], (i - 0.3, 0.6), facecolors=colors['running'])

            ax.text(wait_start + wait_time / 2, i, f'Wait: {wait_time:.2f}', va='center', ha='center', color='black')
            ax.text(run_start + run_time / 2, i, f'Run: {run_time:.2f}', va='center', ha='center', color='white')
            ax.text(done_time + 1, i, f'Total: {total_time:.2f}', va='center', ha='left', color='blue')

        total_time_spent = max_end_time - min_start_time

        ax.set_yticks(y_positions)
        ax.set_yticklabels([job['subdir'] for job in self])
        ax.set_xlabel("Time (seconds)")
        ax.set_title(f"Job Schedule Visualization (Total Time: {total_time_spent:.2f} seconds)")

        legend_patches = [mpatches.Patch(color=colors[key], label=key.capitalize()) for key in colors]
        ax.legend(handles=legend_patches, loc='lower right', bbox_to_anchor=(1, 0))

        plt.show(block=True)  # Keeps the window open until manually closed
   
    @lock_sync
    def save_to_csv(self, filepath):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Define the main header
            header_main = [
                'command', 'subdir', 'status', 'approved', 'adviser', 'process', 'process_info',
                'process_info', 'process_info', 'process_info', 'process_info', 'process_info', 'process_info',
                'process_info', 'process_info', 'process_info', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times',
                'adviser_response', 'adviser_response', 'adviser_response', 'pid'
            ]
            
            # Define the sub-header
            header_sub = ['', '', '', '', '', '', 'pid', 'memory', 'memory', 'memory', 'cpu', 'cpu', '', '', '',
                          'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', '', '', '', '']
            
            # Define the third header row
            header_third = ['', '', '', '', '', '', '', 'rss', 'vms', 'percent', 'percent', 'num', 'waitq_start_time', 'runq_start_time', 'doneq_start_time',
                            'user', 'system', 'children_user', 'children_system', 'iowait', 'get_worker_info', 'worker_resource_config', 'change_worker', '']
            
            # Write header rows
            writer.writerow(header_main)
            writer.writerow(header_sub)
            writer.writerow(header_third)
            
            # Write data rows
            for item in self:
                process_info = item['process_info']
                adviser_response = item['adviser_response']
                
                row = [
                    item['command'],
                    item['subdir'],
                    item['status'],
                    ','.join(item['approved']) if isinstance(item['approved'], list) else item['approved'],
                    item['adviser'],
                    str(item['process']),
                    process_info.get('pid', 0)
                ]
                
                # Append process_info values
                row.extend([
                    process_info.get('memory_rss', 0),
                    process_info.get('memory_vms', 0),
                    process_info.get('memory_percent', 0),
                    process_info.get('cpu_percent', 0),
                    process_info.get('cpu_num', 0),
                    process_info.get('waitq_start_time', 0),
                    process_info.get('runq_start_time', 0),
                    process_info.get('doneq_start_time', 0)
                ])
                
                # Append cpu_times values
                cpu_times = process_info.get('cpu_times', {})
                row.extend([getattr(cpu_times, key, 0) for key in ['user', 'system', 'children_user', 'children_system', 'iowait']])
                
                # Append adviser_response values
                row.extend([adviser_response.get(key, 'NA') for key in ['get_worker_info', 'worker_resource_config', 'change_worker']])
                
                # Append final pid column
                row.append(item.get('pid', 0))
                
                writer.writerow(row)
        
        if self.verbose:
            print(f"Queue information saved to {filepath}")
