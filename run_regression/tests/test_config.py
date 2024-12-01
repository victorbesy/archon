# test_config.py
import unittest
import os
import datetime
from unittest.mock import patch, MagicMock
from config import Config
from queues import SmartQ

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.regression_config = {'regression_name': 'test_regression'}
        self.config = Config(self.regression_config)

    @patch('os.makedirs')
    @patch('datetime.datetime')
    def test_create_directory(self, mock_datetime, mock_makedirs):
        mock_now = MagicMock()
        mock_now.strftime.return_value = '20230930_155300'
        mock_datetime.now.return_value = mock_now
        self.config.create_directory()
        expected_dir = 'test_regression_20230930_155300'
        mock_makedirs.assert_called_once_with(expected_dir, exist_ok=True)
        self.assertEqual(self.config.root_dir, expected_dir)

    def test_fill_queues(self):
        compile_commands = {'commands': [{'command': 'compile_cmd1', 'subdir': 'subdir1'}]}
        run_commands = {'commands': [{'command': 'run_cmd1', 'subdir': 'subdir2'}]}
        self.config.fill_queues(compile_commands, run_commands)

        compile_item = self.config.compile_wait_queue.get()
        self.assertEqual(compile_item['command'], 'compile_cmd1')
        self.assertEqual(compile_item['subdir'], 'subdir1')
        self.assertEqual(compile_item['approved'], ['CompRunQMng'])

        run_item = self.config.test_wait_queue.get()
        self.assertEqual(run_item['command'], 'run_cmd1')
        self.assertEqual(run_item['subdir'], 'subdir2')
        self.assertEqual(run_item['approved'], [])

    def test_set_status_wait(self):
        q = SmartQ()
        q.put({'command': 'cmd1', 'status': ''})
        q.put({'command': 'cmd2', 'status': ''})
        self.config.set_status_wait(q)
        
        item1 = q.get()
        self.assertEqual(item1['status'], 'wait')
        item2 = q.get()
        self.assertEqual(item2['status'], 'wait')

    @patch('builtins.print')
    def test_print_queue(self, mock_print):
        q = SmartQ()
        q.put({'command': 'cmd1'})
        q.put({'command': 'cmd2'})
        self.config.print_queue(q, 'Test')
        
        mock_print.assert_any_call('Test queue:')
        mock_print.assert_any_call({'command': 'cmd1'})
        mock_print.assert_any_call({'command': 'cmd2'})

    def test_find_list_entry_index(self):
        in_list = ['entry1', 'entry2', 'entry3']
        index = self.config.find_list_entry_index(in_list, 'entry2')
        self.assertEqual(index, 1)

    def test_remove_list_entry_by_index(self):
        in_list = ['entry1', 'entry2', 'entry3']
        updated_list = self.config.remove_list_entry_by_index(in_list, 1)
        self.assertEqual(updated_list, ['entry1', 'entry3'])
        self.assertFalse(self.config.remove_list_entry_by_index(in_list, 5))

if __name__ == '__main__':
    unittest.main()
