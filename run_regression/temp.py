import queue

class ExtendedQueue(queue.Queue):
    def remove(self, item):
        with self.mutex:
            try:
                self.queue.remove(item)
                return 0
            except ValueError:
                return -1

# Example usage
if __name__ == "__main__":
    q = ExtendedQueue()
    q.put(10)
    q.put(20)
    q.put(30)
    
    print("Queue before removal:", list(q.queue))  # Output: Queue before removal: [10, 20, 30]
    result = q.remove(20)
    print("Remove result:", result)  # Output: Remove result: 0
    print("Queue after removal:", list(q.queue))  # Output: Queue after removal: [10, 30]
    
    result = q.remove(40)  # This will return -1
    print("Remove result:", result)  # Output: Remove result: -1
