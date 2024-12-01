import queue
import threading

class SmartQ(queue.Queue):
    def __init__(self, verbose=False, name="NA"):
        super().__init__()
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

    def put(self, item, block=True, timeout=None, release=True):
        self._acquire_lock('put')
        try:
            return super().put(item, block, timeout)
        finally:
            self._release_lock('put', release)

    def get(self, block=True, timeout=None, release=True):
        self._acquire_lock('get')
        try:
            return super().get(block, timeout)
        finally:
            self._release_lock('get', release)

    def peek(self, release=True):
        self._acquire_lock('peek')
        try:
            if self.queue:
                return self.queue[0]
        finally:
            self._release_lock('peek', release)

    def remove(self, item, release=True):
        self._acquire_lock('remove')
        try:
            self.queue.remove(item)
            return 0
        except ValueError:
            return -1
        finally:
            self._release_lock('remove', release)

    def iter_queue(self, release=True):
        self._acquire_lock('iter_queue')
        try:
            snapshot = list(self.queue)
            for item in snapshot:
                yield item
        finally:
            self._release_lock('iter_queue', release)

    def iter_conditional(self, condition, release=True):
        self._acquire_lock('iter_conditional')
        try:
            for item in list(self.queue):
                if condition(item):
                    yield item
        finally:
            self._release_lock('iter_conditional', release)

    def is_empty(self, release=True):
        self._acquire_lock('is_empty')
        try:
            return super().empty()
        finally:
            self._release_lock('is_empty', release)
    def print_queue(self,prefix=""):
        self._acquire_lock('print_queue')
        try:
            if self.queue:
                print(f"{prefix} {self._name} queue:")
                for item in self.queue:
                    print(item)
            else:
                print(f"{self._name} queue: Empty")
        finally:
            self._release_lock('print_queue')

