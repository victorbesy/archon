import threading
import queue
import time
import random
import icecream 

# 4. Modified SmartQ class for broadcast messaging
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
                    self.get()  # Remove message once all have read it

broadcast_queue = SmartQ()

# Base thread class with broadcast capabilities
class ThreadWithBroadcast(threading.Thread):
    def __init__(self, name, broadcast_queue):
        super().__init__()
        self.name = name
        self.broadcast_queue = broadcast_queue

    def run(self):
        self.configure_thread()
        while True:
            message = self.broadcast_queue.peek()
            if message and not message['status'][self.name]:
                self.print_message(message)
                self.broadcast_queue.confirm_read_and_maybe_remove(self.name)
            else:
                time.sleep(1)  # 6.2 Wait if no new message
            self.generate_and_send_message()

    def configure_thread(self):
        print(f"{self.name} is configured and running.")

    def print_message(self, message):
        # Improved print function to include ID, instruction, and queue entry
        print(f"{self.name} received message ID {message['id']}: {message['instruction']} from {message['sender']} | Queue Entry: {message}")

    def generate_and_send_message(self):
        with self.broadcast_queue.lock:
            if (broadcast_queue.empty() or all(broadcast_queue.queue[-1]['status'].values())) and random.random() < 0.1:
                instructions = ["stop thread", "run thread", "wait for the next message", "exit thread"]
                message = {
                    'id': random.randint(1, 10000),  # Unique ID for the message
                    'instruction': random.choice(instructions),
                    'sender': self.name,
                    'status': {thread.name: False for thread in threads},
                }
                broadcast_queue.put(message)

threads = [
    ThreadWithBroadcast("CompDoneQMgr", broadcast_queue),
    ThreadWithBroadcast("CompRunQMgr", broadcast_queue),
    ThreadWithBroadcast("CompWatchdog", broadcast_queue),
    ThreadWithBroadcast("RuntimeTestMonitor", broadcast_queue),
    ThreadWithBroadcast("RuntimeTestMgr", broadcast_queue),
    ThreadWithBroadcast("RuntimeTestWatchdog", broadcast_queue),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
