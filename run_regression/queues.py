import threading
from collections import deque
from functools import wraps

def lock_sync(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self.lock:
            return func(self, *args, **kwargs)
    return wrapper

class SmartQ(deque):
    def __init__(self, verbose=True, name="NA"):
        super().__init__()
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
                'future': ''
            })
        if self.verbose:
            print(f"{self._name} queue initialized with commands")

    @lock_sync
    def set_queue_default(self, approved, adviser, status):
        for item in self:
            item['adviser'] = [adviser]
            item['status'] = [status]
            item['approved'] = [approved]
        if self.verbose:
            print(f"Adviser set to {adviser}, approved set to {approved}, and status set to {status} for all items in {self._name} queue")

    @lock_sync
    def set_adviser(self, item, adviser):
        item['adviser'] = adviser
        if self.verbose:
            print(f"Adviser set to {adviser} for item in {self._name} queue")

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
    def get_adviser(self, item):
        adviser = item['adviser'] if item['adviser'] else False
        if self.verbose:
            print(f"Adviser of item in {self._name} queue: {adviser}")
        return adviser

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