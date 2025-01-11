import queue
import threading

class SmartQ(queue.Queue):
    def __init__(self, verbose=False, name="NA"):
        super().__init__()
        self.lock = threading.Lock()
        self.current_owner = None
        self.verbose = verbose
        self._name = name
        self.global_lock_acquired = False

    def get_size(self):
        if not self.global_lock_acquired:
            self._acquire_lock("get_size")
        size = self.qsize()
        if not self.global_lock_acquired:
            self._release_lock("get_size")
        return size

    def _acquire_lock(self, function_name):
        current_thread = threading.current_thread().name
        if self.current_owner and self.current_owner != current_thread:
            print(f"Warning: {current_thread} is waiting to access the {self._name} SmartQ in {function_name} while it's owned by {self.current_owner}")
            while self.current_owner and self.current_owner != current_thread:
                pass
        self.lock.acquire()
        self.current_owner = current_thread
        if self.verbose:
            print(f"{current_thread} has locked the {self._name} SmartQ in {function_name}")

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
        self._acquire_lock(function_name)
        self.global_lock_acquired = True

    def release_lock(self, function_name="release_lock"):
        if not self.global_lock_acquired:
            return
        self.global_lock_acquired = False
        self._release_lock(function_name)

    def put(self, item, block=True, timeout=None):
        if not self.global_lock_acquired:
            self._acquire_lock('put')
        try:
            return super().put(item, block, timeout)
        finally:
            if not self.global_lock_acquired:
                self._release_lock('put')

    def get(self, block=True, timeout=None):
        if not self.global_lock_acquired:
            self._acquire_lock('get')
        try:
            return super().get(block, timeout)
        finally:
            if not self.global_lock_acquired:
                self._release_lock('get')

    def peek(self):
        if not self.global_lock_acquired:
            self._acquire_lock('peek')
        try:
            if self.queue:
                return self.queue[0]
        finally:
            if not self.global_lock_acquired:
                self._release_lock('peek')

    def remove(self, item):
        if not self.global_lock_acquired:
            self._acquire_lock('remove')
        try:
            self.queue.remove(item)
            return 0
        except ValueError:
            return -1
        finally:
            if not self.global_lock_acquired:
                self._release_lock('remove')

    def iter_queue(self):
        if not self.global_lock_acquired:
            self._acquire_lock('iter_queue')
        try:
            snapshot = list(self.queue)
            for item in snapshot:
                yield item
        finally:
            if not self.global_lock_acquired:
                self._release_lock('iter_queue')

    def iter_conditional(self, condition):
        if not self.global_lock_acquired:
            self._acquire_lock('iter_conditional')
        try:
            for item in list(self.queue):
                if condition(item):
                    yield item
        finally:
            if not self.global_lock_acquired:
                self._release_lock('iter_conditional')

    def is_empty(self):
        if not self.global_lock_acquired:
            self._acquire_lock('is_empty')
        try:
            return super().empty()
        finally:
            if not self.global_lock_acquired:
                self._release_lock('is_empty')

    def print_queue(self, prefix=""):
        if not self.global_lock_acquired:
            self._acquire_lock('print_queue')
        try:
            if self.queue:
                print(f"{prefix} {self._name} queue:")
                for item in self.queue:
                    print(item)
            else:
                print(f"{self._name} queue: Empty")
        finally:
            if not self.global_lock_acquired:
                self._release_lock('print_queue')
