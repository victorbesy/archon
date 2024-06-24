import argparse
import os
import toml
import random

def generate_compile_commands(regression_config):
    compile_commands = []
    for module_name, module in regression_config['modulelist'].items():
        module_compile_args = module.get('comp_makeargs', '')
        for group in module['groups']:
            group_compile_args = group.get('comp_makeargs', '')
            compile_cmd = f"make {module_compile_args} {group_compile_args}"
            compile_commands.append(compile_cmd.strip())
    return compile_commands

def generate_run_commands(regression_config):
    run_commands = []
    for module_name, module in regression_config['modulelist'].items():
        module_run_args = module.get('run_makeargs', '')
        for group in module['groups']:
            group_run_args = group.get('run_makeargs', '')
            for test in group['testlist']:
                test_name_no_ext = os.path.splitext(test['testfile'])[0]
                seed = test.get('seed', 'random')
                repeat_count = test.get('repeat', 1)

                test_run_args = test.get('runargs', '')
                test_make_args = test.get('makeargs', '')

                if seed != 'random':
                    run_cmd = f"make TEST={test_name_no_ext} SEED={seed} GROUP={group['name']} TEST_NAME={test['testname']} {module_run_args} {group_run_args} {test_run_args} {test_make_args}"
                    run_commands.append(run_cmd.strip())
                else:
                    for i in range(repeat_count):
                        random_seed = random.randint(100000, 999999)  # Generate a long random number
                        run_cmd = f"make TEST={test_name_no_ext} SEED={random_seed} GROUP={group['name']} TEST_NAME={test['testname']} {module_run_args} {group_run_args} {test_run_args} {test_make_args}"
                        run_commands.append(run_cmd.strip())
    return run_commands

def write_commands_to_file(commands, filename):
    with open(filename, 'w') as file:
        for command in commands:
            file.write(command + "\n")

# Main Execution
if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser(description='Generate Test Command Lines')
    parser.add_argument('-regression_config', required=True, help='Path to regression config file')
    parser.add_argument('-system_config', required=True, help='Path to system config file')
    args = parser.parse_args()

    # Load Configuration Files
    regression_config = toml.load(open(args.regression_config))
    system_config = toml.load(open(args.system_config))

    # Generate Compile and Run Commands
    compile_commands = generate_compile_commands(regression_config)
    run_commands = generate_run_commands(regression_config)

    # Write Commands to Files
    write_commands_to_file(compile_commands, 'CompileCommands.txt')
    write_commands_to_file(run_commands, 'RunCommands.txt')

    print("Compile and run commands have been generated and saved to 'CompileCommands.txt' and 'RunCommands.txt'.")
