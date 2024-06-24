import os
import shutil
import toml
import argparse
from datetime import datetime

class Init:
    def __init__(self):
        # Parse command line arguments
        args = self.parse_arguments()
        self.system_config = self.read_config(args.system_config)
        self.regression_config = self.read_config(args.regression_config)

        # Create directories and copy makefiles
        self.create_directories_and_copy_makefiles()

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-regression_config', required=True)
        parser.add_argument('-system_config', required=True)
        return parser.parse_args()

    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            return toml.load(file)

    def create_directories_and_copy_makefiles(self):
        regression_name = self.regression_config['regression_name']
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        main_dir = f"{regression_name}_{timestamp}"
        os.makedirs(main_dir, exist_ok=True)

        for module_key, module_val in self.regression_config['modulelist'].items():
            for group in module_val['groups']:
                group_dir = os.path.join(main_dir, group['name'])
                os.makedirs(group_dir, exist_ok=True)

                build_dir = os.path.join(group_dir, 'build')
                tests_dir = os.path.join(group_dir, 'tests')
                os.makedirs(build_dir, exist_ok=True)
                os.makedirs(tests_dir, exist_ok=True)

                for test in group['testlist']:
                    test_build_dir = os.path.join(build_dir, f"{test['testname']}_{test['seed']}")
                    test_test_dir = os.path.join(tests_dir, f"{test['testname']}_{test['seed']}")

                    os.makedirs(test_build_dir, exist_ok=True)
                    os.makedirs(test_test_dir, exist_ok=True)

                    # Copy makefiles
                    #shutil.copy(self.system_config['script']['compile_makefile'], test_build_dir)
                    #shutil.copy(self.system_config['script']['run_makefile'], test_test_dir)

# Example usage
init = Init()
