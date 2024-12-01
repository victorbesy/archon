# test_artifact_run_q_arb_ex.py
'''
import unittest
from artifact_run_q_arb_ex import ArtifactRunQArbEx
from queues import SmartQ
from unittest.mock import patch, MagicMock

class TestArtifactRunQArbEx(unittest.TestCase):

    def setUp(self):
        self.config = MagicMock()
        self.system_config = {'script': {'concurrent_run': 2, 'test_makefile': '/test_makefile'}}
        self.artifact_run = ArtifactRunQArbEx(self.config, self.system_config)

    def test_set_makefile_path(self):
        self.artifact_run.set_makefile_path('/test_makefile')
        self.assertEqual(self.artifact_run.get_makefile_path(), '/test_makefile')

    def test_set_max_concurrent_task(self):
        self.artifact_run.set_max_concurrent_task(3)
        self.assertEqual(self.artifact_run.get_max_concurrent_task(), 3)

    def test_run_with_no_makefile(self):
        with self.assertRaises(ValueError):
            self.artifact_run.run()

    def test_process_task(self):
        with patch('subprocess.run') as mock_run:
            self.artifact_run.set_makefile_path('/test_makefile')
            self.artifact_run.set_wait_queue(SmartQ())
            self.artifact_run.set_run_queue(SmartQ())
            self.artifact_run.process_task()
            self.assertTrue(mock_run.called)

if __name__ == '__main__':
    unittest.main()
'''