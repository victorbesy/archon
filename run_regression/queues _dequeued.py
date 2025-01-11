import threading
from collections import deque

class SmartQ:
    def __init__(self, verbose=False, name="NA"):
        self.lock = threading.Lock()
        self.queue = deque()
        self.current_owner = None
        self.verbose = verbose
        self._name = name

    def _acquire_lock(self, function_name):
        current_thread = threading.current_thread().name
        if self.current_owner and self.current_owner != current_thread:
            print(f"Warning: {current_thread} is trying to access the {self._name} SmartQ in {function_name} while it's owned by {self.current_owner}")
        self.lock.acquire()
        self.current_owner = current_thread
        if self.verbose:
            print(f"{current_thread} has locked the {self._name} SmartQ in {function_name}")

    def _release_lock(self, function_name):
        if self.verbose:
            print(f"{self.current_owner} has released the {self._name} SmartQ in {function_name}")
        self.current_owner = None
        self.lock.release()

    def put(self, item):
        self._acquire_lock('put')
        try:
            self.queue.append(item)
            if self.verbose:
                print(f"Item {item} added to {self._name} queue")
        finally:
            self._release_lock('put')

    def get(self):
        self._acquire_lock('get')
        try:
            if self.queue:
                item = self.queue.popleft()
                if self.verbose:
                    print(f"Item {item} removed from {self._name} queue")
                return item
            else:
                if self.verbose:
                    print(f"{self._name} queue is empty")
                return None
        finally:
            self._release_lock('get')

    def peek(self):
        self._acquire_lock('peek')
        try:
            return self.queue[0] if self.queue else None
        finally:
            self._release_lock('peek')

    def remove(self, item):
        self._acquire_lock('remove')
        try:
            try:
                self.queue.remove(item)
                if self.verbose:
                    print(f"Item {item} removed from {self._name} queue")
                return 0
            except ValueError:
                if self.verbose:
                    print(f"Item {item} not found in {self._name} queue")
                return -1
        finally:
            self._release_lock('remove')

    def is_empty(self):
        self._acquire_lock('is_empty')
        try:
            return len(self.queue) == 0
        finally:
            self._release_lock('is_empty')

    def print_queue(self, prefix=""):
        self._acquire_lock('print_queue')
        try:
            if self.queue:
                print(f"{prefix} {self._name} queue: {list(self.queue)}")
            else:
                print(f"{self._name} queue: Empty")
        finally:
            self._release_lock('print_queue')

    def rotate(self):
        self._acquire_lock('rotate')
        try:
            if self.queue:
                first_item = self.queue.popleft()
                self.queue.append(first_item)
                if self.verbose:
                    print(f"Pushed first item {first_item} to end in {self._name} queue")
            else:
                if self.verbose:
                    print(f"{self._name} queue is empty, nothing to push")
        finally:
            self._release_lock('rotate')

    def push_item_back(self, item):
        self._acquire_lock('push_item_back')
        try:
            if item in self.queue:
                self.queue.remove(item)
                self.queue.append(item)
                if self.verbose:
                    print(f"Pushed item {item} to end in {self._name} queue")
            else:
                if self.verbose:
                    print(f"Item {item} not found in {self._name} queue")
        finally:
            self._release_lock('push_item_back')
