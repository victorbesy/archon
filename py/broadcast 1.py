import threading
import queue
import time
import random

# 4. SmartQ class modified to include broadcast functionality
class SmartQ(queue.Queue):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
    
    def peek(self):
        with self.lock:
            return self.queue[0] if not self.empty() else None

    def confirm_read_and_maybe_remove(self, reader):
        with self.lock:
            if not self.empty():
                message = self.queue[0]
                message['status'][reader] = True
                if all(message['status'].values()):
                    self.get()  # Remove message once all have read

global_broadcast_queue = SmartQ()

# 1. Thread classes
class ThreadWithBroadcast(threading.Thread):
    def __init__(self, name, broadcast_queue):
        super().__init__()
        self.name = name
        self.broadcast_queue = broadcast_queue
        self.message_seen = set()  # To track which messages have been seen

    def run(self):
        # 5. Configuration function
        self.configure_thread()
        while True:
            # 6.1 Check for new broadcast message
            message = self.broadcast_queue.peek()
            if message and message['id'] not in self.message_seen:
                self.message_seen.add(message['id'])
                # 6.3 Print function
                self.print_message(message)
                self.broadcast_queue.confirm_read_and_maybe_remove(self.name)
                # 6.4 Jump to the beginning of the loop
            else:
                # 6.2 Wait if no new message
                time.sleep(1)
            # 7. Randomly generate and send broadcast messages
            self.generate_and_send_message()

    def configure_thread(self):
        print(f"{self.name} is configured and running.")

    def print_message(self, message):
        print(f"{self.name} received message: {message}")

    def generate_and_send_message(self):
        if random.randint(0, 10) < 2:  # Randomly decide to send a message or not
            with self.broadcast_queue.lock:
                if self.broadcast_queue.empty() or self.broadcast_queue.queue[-1]['future'] == len(threads):
                    message = {
                        'id': random.randint(1000, 9999),
                        'content': random.choice(["stop thread", "run thread", "wait for the next message", "exit thread"]),
                        'status': {t.name: False for t in threads},
                        'future': 0
                    }
                    self.broadcast_queue.put(message)
                    print(f"{self.name} sent a message: {message}")

threads = [
    ThreadWithBroadcast("CompDoneQMgr", global_broadcast_queue),
    ThreadWithBroadcast("CompRunQMgr", global_broadcast_queue),
    ThreadWithBroadcast("CompWatchdog", global_broadcast_queue),
    ThreadWithBroadcast("RuntimeTestMonitor", global_broadcast_queue),
    ThreadWithBroadcast("RuntimeTestMgr", global_broadcast_queue),
    ThreadWithBroadcast("RuntimeTestWatchdog", global_broadcast_queue),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
