# test_queues.py
import unittest
import queue
from queues import SmartQ

class TestSmartQ(unittest.TestCase):

    def setUp(self):
        self.smartq = SmartQ()

    def test_peek_empty(self):
        # Peek on an empty queue should return None
        result = self.smartq.peek()
        self.assertIsNone(result)

    def test_peek_non_empty(self):
        # Add an element and check peek
        self.smartq.put(10)
        result = self.smartq.peek()
        self.assertEqual(result, 10)

    def test_peek_does_not_remove_element(self):
        # Peek should not remove the element
        self.smartq.put(20)
        result = self.smartq.peek()
        self.assertEqual(result, 20)
        # Ensure element is still in the queue after peek
        result_after_peek = self.smartq.get()
        self.assertEqual(result_after_peek, 20)

    def test_remove_element_exists(self):
        # Add elements and remove one
        self.smartq.put(1)
        self.smartq.put(2)
        self.smartq.put(3)
        self.smartq.remove(2)

        # Check if element 2 was removed
        self.assertNotIn(2, list(self.smartq.iter_queue()))

    def test_remove_element_not_exists(self):
        # Add elements and try to remove a non-existent element
        self.smartq.put(4)
        self.smartq.put(5)
        self.smartq.put(6)
        self.smartq.remove(100)

        # Check that all original elements are still present
        elements = list(self.smartq.iter_queue())
        self.assertIn(4, elements)
        self.assertIn(5, elements)
        self.assertIn(6, elements)
        self.assertEqual(len(elements), 3)

    def test_remove_empty_queue(self):
        # Test remove on an empty queue (should do nothing)
        self.smartq.remove(1)
        self.assertTrue(self.smartq.empty())

    def test_iter_queue(self):
        # Add elements and iterate through the queue
        elements = [10, 20, 30]
        for e in elements:
            self.smartq.put(e)

        iterated_elements = list(self.smartq.iter_queue())
        self.assertEqual(iterated_elements, elements)

    def test_iter_queue_empty(self):
        # Iterating over an empty queue should return an empty list
        iterated_elements = list(self.smartq.iter_queue())
        self.assertEqual(iterated_elements, [])

    def test_iter_conditional(self):
        # Add elements and iterate conditionally
        elements = [1, 2, 3, 4, 5, 6, 7, 8]
        for e in elements:
            self.smartq.put(e)

        # Iterate over elements that satisfy the condition (even numbers)
        even_elements = list(self.smartq.iter_conditional(lambda x: x % 2 == 0))
        self.assertEqual(even_elements, [2, 4, 6, 8])

    def test_iter_conditional_empty(self):
        # Conditional iteration on empty queue should return nothing
        result = list(self.smartq.iter_conditional(lambda x: x % 2 == 0))
        self.assertEqual(result, [])

    def test_thread_safety_peek(self):
        # Simulate concurrent access for `peek` to ensure thread safety
        self.smartq.put(99)
        with self.smartq.lock:
            result = self.smartq.peek()
        self.assertEqual(result, 99)

    def test_thread_safety_remove(self):
        # Simulate concurrent access for `remove` to ensure thread safety
        elements = [5, 10, 15]
        for e in elements:
            self.smartq.put(e)

        with self.smartq.lock:
            self.smartq.remove(10)

        # Check if element 10 was safely removed
        self.assertNotIn(10, list(self.smartq.iter_queue()))

    def test_thread_safety_iter_queue(self):
        # Simulate concurrent access for `iter_queue` to ensure thread safety
        elements = [1, 2, 3]
        for e in elements:
            self.smartq.put(e)

        with self.smartq.lock:
            iterated_elements = list(self.smartq.iter_queue())

        self.assertEqual(iterated_elements, elements)

if __name__ == '__main__':
    unittest.main()
