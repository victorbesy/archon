import unittest
from unittest.mock import MagicMock, patch
from watchdogs import Watchdog
from queues import SmartQ
import time

class TestWatchdog(unittest.TestCase):

    def setUp(self):
        self.config_mock = MagicMock()
        self.system_config_mock = MagicMock()
        self.watchdog = Watchdog(self.config_mock, self.system_config_mock)

    def test_set_start(self):
        self.watchdog.set_start(5)
        self.assertEqual(self.watchdog.get_start(), 5)

    def test_set_eot_mode_valid(self):
        self.watchdog.set_eot_mode('compile')
        self.assertEqual(self.watchdog.get_eot_mode(), 'compile')

        self.watchdog.set_eot_mode('run')
        self.assertEqual(self.watchdog.get_eot_mode(), 'run')

    def test_set_eot_mode_invalid(self):
        with self.assertRaises(ValueError):
            self.watchdog.set_eot_mode('invalid_mode')

    def test_update_eot_compile_mode(self):
        self.watchdog.set_eot_mode('compile')
        self.config_mock.compile_eot = True
        self.assertTrue(self.watchdog.update_eot())

    def test_update_eot_run_mode(self):
        self.watchdog.set_eot_mode('run')
        self.config_mock.test_eot = True
        self.assertTrue(self.watchdog.update_eot())

    def test_update_eot_no_mode(self):
        with self.assertRaises(ValueError):
            self.watchdog.update_eot()

    def test_set_max_timeout(self):
        self.watchdog.set_max_timeout(100)
        self.assertEqual(self.watchdog.get_max_timeout(), 100)

    def test_set_name(self):
        self.watchdog.set_name('TestWatchdog')
        self.assertEqual(self.watchdog.get_name(), 'TestWatchdog')

    def test_set_wait_queue(self):
        queue = SmartQ()
        self.watchdog.set_wait_queue(queue)
        self.assertEqual(self.watchdog._wait_queue, queue)

    def test_set_run_queue(self):
        queue = SmartQ()
        self.watchdog.set_run_queue(queue)
        self.assertEqual(self.watchdog._run_queue, queue)

    def test_set_done_queue(self):
        queue = SmartQ()
        self.watchdog.set_done_queue(queue)
        self.assertEqual(self.watchdog._done_queue, queue)

    def test_run_no_max_timeout(self):
        self.watchdog.set_max_timeout(0)
        with self.assertRaises(ValueError):
            self.watchdog.run()

    @patch('time.time', side_effect=[0, 1, 2, 3, 4, 5])
    def test_run_with_max_timeout(self, mock_time):
        self.watchdog.set_max_timeout(60)
        self.watchdog.set_eot_mode('run')
        self.config_mock.test_eot = False

        self.watchdog.set_start(1)
        self.watchdog.set_name('TestWatchdog')

        with patch.object(self.watchdog, 'update_eot', side_effect=[False, False, False, False, True]):
            self.watchdog.run()

        self.config_mock.print_queue.assert_any_call(self.watchdog._wait_queue, "wait")
        self.config_mock.print_queue.assert_any_call(self.watchdog._run_queue, "run")
        self.config_mock.print_queue.assert_any_call(self.watchdog._done_queue, "done")

if __name__ == '__main__':
    unittest.main()
