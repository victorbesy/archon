import queue
import threading
from collections import deque

class SmartQ(queue.Queue):
    def __init__(self, verbose=False, name="NA"):
        super().__init__()
        self.queue = deque()
        self.lock = threading.Lock()
        self.current_owner = None
        self.verbose = verbose
        self._name = name

    def _acquire_lock(self, function_name):
        current_thread = threading.current_thread().name
        if self.current_owner:
            if self.current_owner != current_thread:
                print(f"Warning: {current_thread} is trying to access the {self._name} SmartQ in {function_name} while it's owned by {self.current_owner}")
                return False
        self.lock.acquire()
        self.current_owner = current_thread
        if self.verbose:
            print(f"{current_thread} has locked the {self._name} SmartQ in {function_name}")
        return True

    def _release_lock(self, function_name):
        current_thread = threading.current_thread().name
        if self.current_owner != current_thread:
            print(f"Warning: {current_thread} is trying to release the {self._name} SmartQ in {function_name} which is owned by {self.current_owner}")
            return
        if self.verbose:
            print(f"{current_thread} has released the {self._name} SmartQ in {function_name}")
        self.current_owner = None
        self.lock.release()

    def acquire_lock(self, function_name="acquire_lock"):
        if not self._acquire_lock(function_name):
            raise RuntimeError(f"Lock already acquired by {self.current_owner}")

    def release_lock(self, function_name="release_lock"):
        self._release_lock(function_name)

    def put(self, item, block=True, timeout=None):
        if not self._acquire_lock('put'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            return super().put(item, block, timeout)
        finally:
            self._release_lock('put')

    def get(self, block=True, timeout=None):
        if not self._acquire_lock('get'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            return super().get(block, timeout)
        finally:
            self._release_lock('get')

    def peek(self):
        if not self._acquire_lock('peek'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            if self.queue:
                return self.queue[0]
        finally:
            self._release_lock('peek')

    def remove(self, item):
        if not self._acquire_lock('remove'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            self.queue.remove(item)
            return 0
        except ValueError:
            return -1
        finally:
            self._release_lock('remove')

    def iter_queue(self):
        if not self._acquire_lock('iter_queue'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            snapshot = list(self.queue)
            for item in snapshot:
                yield item
        finally:
            self._release_lock('iter_queue')

    def iter_conditional(self, condition):
        if not self._acquire_lock('iter_conditional'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            for item in list(self.queue):
                if condition(item):
                    yield item
        finally:
            self._release_lock('iter_conditional')

    def is_empty(self):
        if not self._acquire_lock('is_empty'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            return super().empty()
        finally:
            self._release_lock('is_empty')

    def print_queue(self, prefix=""):
        if not self._acquire_lock('print_queue'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            if self.queue:
                print(f"{prefix} {self._name} queue:")
                for item in self.queue:
                    print(item)
            else:
                print(f"{self._name} queue: Empty")
        finally:
            self._release_lock('print_queue')

    def rotate(self):
        if not self._acquire_lock('rotate'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            if not self.queue:
                if self.verbose:
                    print(f"{self._name} queue: Empty, nothing to rotate")
                return
            first_item = self.queue.popleft()
            self.queue.append(first_item)
            if self.verbose:
                print(f"Rotated first item to end in {self._name} queue")
        finally:
            self._release_lock('rotate')

    def push_item_back(self, item):
        if not self._acquire_lock('push_item_back'):
            raise RuntimeError("Cannot acquire lock, lock already acquired by another thread")
        try:
            if not self.queue:
                if self.verbose:
                    print(f"{self._name} queue: Empty, nothing to push")
                return
            self.queue.remove(item)
            self.queue.append(item)
            if self.verbose:
                print(f"Pushed item {item} to end in {self._name} queue")
        except ValueError:
            if self.verbose:
                print(f"Item {item} not found in {self._name} queue")
        finally:
            self._release_lock('push_item_back')

