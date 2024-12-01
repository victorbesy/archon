import unittest
from unittest.mock import MagicMock, patch, PropertyMock, call
from queues import SmartQ
from comp_run_q_arb_ex import CompRunQArbEx
import os
from io import StringIO
import sys
import os
import shutil
import subprocess
import threading
import concurrent.futures

class TestCompRunQArbEx(unittest.TestCase):

    def setUp(self):
        # Setup mock configuration and system configuration
        self.mock_config = MagicMock()
        self.mock_config.compile_eot = False
        self.mock_config.root_dir = '/mock/root'

        self.mock_system_config = MagicMock()

        # Create instance of CompRunQArbEx
        self.comp_run_q_arb_ex = CompRunQArbEx(self.mock_config, self.mock_system_config)

    def test_set_name(self):
        self.comp_run_q_arb_ex.set_name("TestName")
        self.assertEqual(self.comp_run_q_arb_ex.get_name(), "TestName")

    def test_set_makefile_path(self):
        self.comp_run_q_arb_ex.set_makefile_path("/mock/path")
        self.assertEqual(self.comp_run_q_arb_ex.get_makefile_path(), "/mock/path")

    def test_set_max_concurrent_task(self):
        self.comp_run_q_arb_ex.set_max_concurrent_task(5)
        self.assertEqual(self.comp_run_q_arb_ex.get_max_concurrent_task(), 5)

    def test_set_wait_queue(self):
        mock_wait_queue = MagicMock(SmartQ)
        self.comp_run_q_arb_ex.set_wait_queue(mock_wait_queue)
        self.assertEqual(self.comp_run_q_arb_ex.get_wait_queue(), mock_wait_queue)

    def test_set_run_queue(self):
        mock_run_queue = MagicMock(SmartQ)
        self.comp_run_q_arb_ex.set_run_queue(mock_run_queue)
        self.assertEqual(self.comp_run_q_arb_ex.get_run_queue(), mock_run_queue)

    def test_set_done_queue(self):
        mock_done_queue = MagicMock(SmartQ)
        self.comp_run_q_arb_ex.set_done_queue(mock_done_queue)
        self.assertEqual(self.comp_run_q_arb_ex.get_done_queue(), mock_done_queue)

    @patch('comp_run_q_arb_ex.os._exit')  # Mock os._exit to prevent the process from exiting
    def test_run_missing_makefile_path(self, mock_exit):
        # Simulate missing makefile path
        self.comp_run_q_arb_ex.set_makefile_path('')
        self.comp_run_q_arb_ex.set_wait_queue(MagicMock(SmartQ))
        self.comp_run_q_arb_ex.set_run_queue(MagicMock(SmartQ))
        self.comp_run_q_arb_ex.set_done_queue(MagicMock(SmartQ))

        # Call the run method, ensuring os._exit does not actually exit the test
        self.comp_run_q_arb_ex.run()

        # Check that os._exit(1) was called due to the missing mak

    @patch('comp_run_q_arb_ex.os._exit')  # Mock os._exit to prevent the process from exiting
    def test_run_missing_queues(self, mock_exit):
        # Set a valid makefile path but don't set the queues (they remain None)
        self.comp_run_q_arb_ex.set_makefile_path("/mock/path")
        self.comp_run_q_arb_ex.set_wait_queue(None)
        self.comp_run_q_arb_ex.set_run_queue(None)
        self.comp_run_q_arb_ex.set_done_queue(None)

        # Call the run method, ensuring os._exit does not actually exit the test
        self.comp_run_q_arb_ex.run()

        # Check that os._exit(1) was called due to missing queues
        mock_exit.assert_called_once_with(1)


    @patch('comp_run_q_arb_ex.os.makedirs')
    @patch('comp_run_q_arb_ex.shutil.copy')
    @patch('comp_run_q_arb_ex.subprocess.run')
    def test_process_task(self, mock_subprocess_run, mock_shutil_copy, mock_makedirs):
        # Set up mock queues
        mock_wait_queue = MagicMock(SmartQ)
        mock_run_queue = MagicMock(SmartQ)
        mock_done_queue = MagicMock(SmartQ)

        self.comp_run_q_arb_ex.set_wait_queue(mock_wait_queue)
        self.comp_run_q_arb_ex.set_run_queue(mock_run_queue)
        self.comp_run_q_arb_ex.set_done_queue(mock_done_queue)
        self.comp_run_q_arb_ex.set_makefile_path("/mock/makefile")

        # Create a mock task
        mock_task = {
            'command': 'echo "Hello"',
            'approved': [],
            'subdir': 'subdir1'
        }
        mock_wait_queue.peek.return_value = mock_task
        mock_wait_queue.get.return_value = mock_task

        # Call process_task
        self.comp_run_q_arb_ex.process_task()

        # Verify that makedirs and copy were called
        mock_makedirs.assert_called_once_with('/mock/root/subdir1', exist_ok=True)
        mock_shutil_copy.assert_called_once_with('/mock/makefile', '/mock/root/subdir1')
        
        # Verify subprocess was run
        mock_subprocess_run.assert_called_once_with(['echo', '"Hello"'], cwd='/mock/root/subdir1')
        
        # Verify that task was updated and put into run_queue
        self.assertEqual(mock_task['status'], 'run')
        mock_run_queue.put.assert_called_once_with(mock_task)

@patch('comp_run_q_arb_ex.subprocess.run')
@patch('concurrent.futures.ThreadPoolExecutor.submit')
def test_run_thread_execution(self, mock_executor_submit, mock_subprocess_run):
    # Set up mock queues
    mock_wait_queue = MagicMock(SmartQ)
    mock_run_queue = MagicMock(SmartQ)
    mock_done_queue = MagicMock(SmartQ)

    # Mock queue behavior
    mock_run_queue.qsize.return_value = 0  # Room for tasks in the run queue
    mock_wait_queue.empty.side_effect = [False, True]  # Simulate task present initially, then empty
    mock_run_queue.empty.return_value = False
    mock_done_queue.empty.return_value = True

    # Set up a mock task
    mock_task = {
        'command': 'echo "Hello"',
        'approved': [],
        'subdir': 'subdir1'
    }

    # Mock config and ensure compile_eot remains False for task processing
    self.mock_config.compile_eot = False

    # Set up the object under test
    self.comp_run_q_arb_ex.set_makefile_path("/mock/makefile")
    self.comp_run_q_arb_ex.set_max_concurrent_task(2)
    self.comp_run_q_arb_ex.set_wait_queue(mock_wait_queue)
    self.comp_run_q_arb_ex.set_run_queue(mock_run_queue)
    self.comp_run_q_arb_ex.set_done_queue(mock_done_queue)

    # Ensure the task is fetched from the wait queue
    mock_wait_queue.peek.return_value = mock_task
    mock_wait_queue.get.return_value = mock_task

    # Start the thread
    self.comp_run_q_arb_ex.start()

    # Wait for the thread to finish
    self.comp_run_q_arb_ex.join()

    # Debugging: Check if submit was called
    print(f"submit called: {mock_executor_submit.call_count} times")

    # Verify that the task was submitted to the ThreadPoolExecutor
    mock_executor_submit.assert_called_once_with(mock_subprocess_run, ['echo', '"Hello"'], cwd='/mock/root/subdir1')

    # Ensure compile_eot is set to True after processing the task
    self.assertTrue(self.mock_config.compile_eot)



if __name__ == '__main__':
    unittest.main()
