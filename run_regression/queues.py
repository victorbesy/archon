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
    def __init__(self, verbose=False, name="NA"):
        super().__init__()
        self.lock = threading.Lock()
        self.verbose = verbose
        self._name = name
        if self.verbose:
            print(f"{self._name} queue created")

    @lock_sync
    def get_size(self):
        return len(self)

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
        return None

    @lock_sync
    def peek(self):
        if self:
            return self[0]

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
        return len(self) == 0

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

