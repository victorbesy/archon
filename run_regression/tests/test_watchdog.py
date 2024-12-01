import unittest
from unittest.mock import MagicMock
from watchdogs import Watchdog
from queues import SmartQ

class ConfigMock:
    def __init__(self, compile_eot=False, test_eot=False):
        self.compile_eot = compile_eot
        self.test_eot = test_eot

    def print_queue(self, queue, queue_name):
        print(f"{queue_name} queue: {queue}")

class TestWatchdog(unittest.TestCase):

    def setUp(self):
        self.config_mock = ConfigMock()
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
        self.config_mock.test_eot = False
        self.assertFalse(self.watchdog.update_eot())

    def test_update_eot_mode_not_set(self):
        with self.assertRaises(ValueError):
            self.watchdog.update_eot()

    def test_set_max_timeout(self):
        self.watchdog.set_max_timeout(100)
        self.assertEqual(self.watchdog.get_max_timeout(), 100)

    def test_set_name(self):
        self.watchdog.set_name("test_watchdog")
        self.assertEqual(self.watchdog.get_name(), "test_watchdog")

    def test_set_wait_queue(self):
        mock_queue = SmartQ()
        self.watchdog.set_wait_queue(mock_queue)
        self.assertEqual(self.watchdog._wait_queue, mock_queue)

    def test_set_run_queue(self):
        mock_queue = SmartQ()
        self.watchdog.set_run_queue(mock_queue)
        self.assertEqual(self.watchdog._run_queue, mock_queue)

    def test_set_done_queue(self):
        mock_queue = SmartQ()
        self.watchdog.set_done_queue(mock_queue)
        self.assertEqual(self.watchdog._done_queue, mock_queue)

    def test_run_timeout(self):
        self.watchdog.set_max_timeout(60)
        self.watchdog.set_name("TestWatchdog")
        self.watchdog._start = 0  # Ensure the watchdog enters the while loop
        self.watchdog.config.print_queue = MagicMock()
        self.watchdog._wait_queue = MagicMock()
        self.watchdog._run_queue = MagicMock()
        self.watchdog._done_queue = MagicMock()

        with self.assertRaises(ValueError):
            self.watchdog.run()

    def test_run_timeout_with_eot(self):
        """Test that watchdog run works and EOT triggers the appropriate print actions."""
        self.watchdog.set_max_timeout(1)
        self.watchdog.set_name("TestWatchdog")
        self.watchdog.set_eot_mode('compile')
        self.config_mock.compile_eot = False

        self.watchdog.config.print_queue = MagicMock()
        self.watchdog._wait_queue = MagicMock()
        self.watchdog._run_queue = MagicMock()
        self.watchdog._done_queue = MagicMock()

        # Simulate that EOT is not reached within the max_timeout
        self.watchdog._start = 1
        self.watchdog.run()

        # Ensure that the queue printing methods are called, regardless of order
        expected_calls = [
            unittest.mock.call(self.watchdog._wait_queue, "wait"),
            unittest.mock.call(self.watchdog._run_queue, "run"),
            unittest.mock.call(self.watchdog._done_queue, "done")
        ]

        self.watchdog.config.print_queue.assert_has_calls(expected_calls, any_order=True)

if __name__ == '__main__':
    unittest.main()
