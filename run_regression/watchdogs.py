import threading
import time
from queues import SmartQ
from icecream import ic
import os

class Watchdog(threading.Thread):
    def __init__(self, config_in, system_config,set_completion_ev):
        super().__init__()
        self.config = config_in
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self._max_timeout = 0
        self._eot = False
        self._eot_mode = ''
        self._start = 1
        self._name = ''
        self._stop_event = threading.Event()
        self.set_completion_ev =set_completion_ev

    def set_start(self, start):
        self._start = start

    def get_start(self):
        return self._start

    def set_eot_mode(self, eot_mode):
        if eot_mode in ['compile', 'run']:
            self._eot_mode = eot_mode
        else:
            raise ValueError("Invalid mode set. Choose either 'compile' or 'run'.")

    def get_eot_mode(self):
        return self._eot_mode

    def update_eot(self):
        if self._eot_mode == 'compile':
            self._eot = self.config.compile_eot
        elif self._eot_mode == 'run':
            self._eot = self.config.test_eot
        else:
            raise ValueError("Mode is not set. Cannot update EOT.")
        return self._eot

    def set_max_timeout(self, max_timeout):
        self._max_timeout = max_timeout

    def get_max_timeout(self):
        return self._max_timeout

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_wait_queue(self, q):
        if isinstance(q, SmartQ):
            self._wait_queue = q

    def set_run_queue(self, q):
        if isinstance(q, SmartQ):
            self._run_queue = q

    def set_done_queue(self, q):
        if isinstance(q, SmartQ):
            self._done_queue = q

    def stop(self):
        self._stop_event.set()

    def run(self):
        if self._max_timeout <= 0:
            raise ValueError("Missing a corresponding max_timeout in script section of system_config")
        start_time = time.time()
        max_timeout = self.get_max_timeout()
        temp = self.update_eot()
        ic(self._name,temp)
        while time.time() - start_time < max_timeout and not self.update_eot():
            if self._stop_event.is_set():
                break
            temp = self.update_eot()
            ic(self._name,temp)
            ic(time.time() - start_time, max_timeout)
            if self._start == 0:
                max_timeout += 1
            time.sleep(1)  # Sleep for a short period to avoid busy waiting

        if not self._eot:
            print(f"{self._name} :: Timeout reached {self.get_max_timeout()} sec.")
            self._wait_queue.print_queue()
            self._run_queue.print_queue()
            self._done_queue.print_queue()
            self.config.set_watchdog_eot()
            if self.set_completion_ev :
                self.set_completion_ev.set()
            ic(self._name, self.set_completion_ev.is_set())
            os._exit(1)
