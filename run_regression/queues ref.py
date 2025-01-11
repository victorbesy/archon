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
        if self.current_owner and self.current_owner != current_thread:
            print(f"Warning: {current_thread} is trying to access the {self._name} SmartQ in {function_name} while it's owned by {self.current_owner}")
        self.lock.acquire()
        self.current_owner = current_thread
        if self.verbose:
            print(f"{current_thread} has locked the {self._name} SmartQ in {function_name}")

    def _release_lock(self, function_name, release=True):
        if release:
            if self.verbose:
                print(f"{self.current_owner} has released the {self._name} SmartQ in {function_name}")
            self.current_owner = None
            self.lock.release()

    def acquire_lock(self, function_name="acquire_lock", acquire=True):
        if acquire:
            self._acquire_lock(function_name)

    def release_lock(self, function_name="release_lock", release=True):
        if release:
            self._release_lock(function_name, release)

    def put(self, item, block=True, timeout=None, release=True, acquire=True):
        if acquire:
            self._acquire_lock('put')
        try:
            return super().put(item, block, timeout)
        finally:
            if release:
                self._release_lock('put')

    def get(self, block=True, timeout=None, release=True, acquire=True):
        if acquire:
            self._acquire_lock('get')
        try:
            return super().get(block, timeout)
        finally:
            if release:
                self._release_lock('get')

    def peek(self, release=True, acquire=True):
        if acquire:
            self._acquire_lock('peek')
        try:
            if self.queue:
                return self.queue[0]
        finally:
            if release:
                self._release_lock('peek')

    def remove(self, item, release=True, acquire=True):
        if acquire:
            self._acquire_lock('remove')
        try:
            self.queue.remove(item)
            return 0
        except ValueError:
            return -1
        finally:
            if release:
                self._release_lock('remove')

    def iter_queue(self, release=True, acquire=True):
        if acquire:
            self._acquire_lock('iter_queue')
        try:
            snapshot = list(self.queue)
            for item in snapshot:
                yield item
        finally:
            if release:
                self._release_lock('iter_queue')

    def iter_conditional(self, condition, release=True, acquire=True):
        if acquire:
            self._acquire_lock('iter_conditional')
        try:
            for item in list(self.queue):
                if condition(item):
                    yield item
        finally:
            if release:
                self._release_lock('iter_conditional')

    def is_empty(self, release=True, acquire=True):
        if acquire:
            self._acquire_lock('is_empty')
        try:
            return super().empty()
        finally:
            if release:
                self._release_lock('is_empty')

    def print_queue(self, prefix="", release=True, acquire=True):
        if acquire:
            self._acquire_lock('print_queue')
        try:
            if self.queue:
                print(f"{prefix} {self._name} queue:")
                for item in self.queue:
                    print(item)
            else:
                print(f"{self._name} queue: Empty")
        finally:
            if release:
                self._release_lock('print_queue')

    def rotate(self, release=True, acquire=True):
        if acquire:
            self._acquire_lock('rotate')
        try:
            if not self.queue:
                if self.verbose:
                    print(f"{self._name} queue: Empty, nothing to rotate")
                return
            first_item = self.queue.popleft()
            self.queue.append(first_item)
            if self.verbose:
                print(f"rotated first item to end in {self._name} queue")
        finally:
            if release:
                self._release_lock('rotate')

    def push_item_back(self, item, release=True, acquire=True):
        if acquire:
            self._acquire_lock('push_item_back')
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
            if release:
                self._release_lock('push_item_back')
