import threading
from collections import deque

class SmartQ(deque):
    def __init__(self, verbose=False, name="NA"):
        super().__init__()
        self.lock = threading.Lock()
        self.verbose = verbose
        self._name = name

    def get_size(self):
        return len(self)

    def put(self, item):
        self.append(item)
        if self.verbose:
            print(f"Item {item} added to {self._name} queue")

    def get(self):
        if self:
            item = self.popleft()
            if self.verbose:
                print(f"Item {item} removed from {self._name} queue")
            return item
        return None

    def peek(self):
        if self:
            return self[0]

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

    def iter_queue(self):
        snapshot = list(self)
        for item in snapshot:
            yield item

    def iter_conditional(self, condition):
        for item in list(self):
            if condition(item):
                yield item

    def is_empty(self):
        return len(self) == 0

    def print_queue(self, prefix=""):
        if self:
            print(f"{prefix} {self._name} queue: {list(self)}")
        else:
            print(f"{self._name} queue: Empty")
