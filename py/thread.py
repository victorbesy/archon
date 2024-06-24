import threading
import queue
import time
import random

# Lock for updating seen_messages safely
seen_lock = threading.Lock()

# Dummy commands for simulation
commands = [
    {'command': 'TestCommand1', 'subdir': 'TestSubdir1'},
    {'command': 'TestCommand2', 'subdir': 'TestSubdir2'},
    {'command': 'TestCommand3', 'subdir': 'TestSubdir3'},
]

class Init:
    def __init__(self):
        self.broadcast_queue = queue.Queue()
        self.seen_messages = {}
        self.num_threads = 6

    def broadcast_message(self, sender, message):
        # Include sender in the message
        message_with_sender = message.copy()
        message_with_sender['sender'] = sender
        with seen_lock:
            # Initialize seen count
            self.seen_messages[message['command']] = 0
        self.broadcast_queue.put(message_with_sender)

    def check_and_print_message(self, receiver_name):
        try:
            message = self.broadcast_queue.get_nowait()
            with seen_lock:
                self.seen_messages[message['command']] += 1
                # If all threads have seen the message, remove it from seen_messages
                if self.seen_messages[message['command']] == self.num_threads:
                    del self.seen_messages[message['command']]
            # Print the message along with the sender's name
            print(f"{receiver_name} received a message from {message['sender']}: {message}")
            self.broadcast_queue.task_done()  # Indicate that the queue item has been processed
        except queue.Empty:
            pass

class WorkerThread(threading.Thread):
    def __init__(self, name, init_instance):
        threading.Thread.__init__(self)
        self.name = name
        self.init = init_instance

    def run(self):
        while True:
            # Check for new message
            self.init.check_and_print_message(self.name)

            # Randomly decide whether to send a new message
            if random.random() < 0.1:  # Adjust probability as needed
                command = random.choice(commands)
                message = {'command': command['command'], 
                           'subdir': command['subdir'], 
                           'status': '', 
                           'future': ''}
                self.init.broadcast_message(self.name, message)
                print(f"{self.name} sent a message: {message}")

            # Wait a bit before checking again
            time.sleep(1)

# Initialize the Init class
init_instance = Init()

# Thread names
thread_names = [
    "CompDoneQMgr_obj",
    "CompRunQMgr_obj",
    "CompWatchdog_obj",
    "RuntimeTestMonitor_obj",
    "RuntimeTestMgr_obj",
    "RuntimeTestWatchdog_obj",
]

# Create and start threads
threads = []
for name in thread_names:
    thread = WorkerThread(name, init_instance)
    thread.start()
    threads.append(thread)

# Note: The script is designed to run continuously. Implementing a shutdown mechanism is recommended.
