import argparse
import os
import shutil
import toml
import random

def generate_compile_commands(regression_config, system_config):
    compile_commands = []
    for module_name, module in regression_config['modulelist'].items():
        for group in module['groups']:
            compile_cmd = {
                "command": f"make {module['comp_makeargs']} {group['comp_makeargs']}",
                "subdir": f"{module_name}/{group['name']}/build"
            }
            compile_commands.append(compile_cmd)
    return compile_commands

def generate_run_commands(regression_config, system_config):
    run_commands = []
    for module_name, module in regression_config['modulelist'].items():
        for group in module['groups']:
            for test in group['testlist']:
                seed = test['seed']
                test_name_no_ext = os.path.splitext(test['testfile'])[0]
                repeat_count = test['repeat'] if seed == 'random' else 1

                for i in range(repeat_count):
                    current_seed = random.randint(100000, 999999) if seed == 'random' else seed
                    test_subdir = f"{group['name']}/tests/{test_name_no_ext}_{current_seed}"
                    run_cmd = {
                        "command": f"make TEST={test_name_no_ext} SEED={current_seed} GROUP={group['name']} TEST_NAME={test['testname']} {module['run_makeargs']} {group['run_makeargs']} {test['runargs']} {test['makeargs']}",
                        "subdir": test_subdir
                    }
                    run_commands.append(run_cmd)
    return run_commands

def write_commands_to_toml(commands, filename):
    toml_data = {"commands": commands}
    with open(filename, 'w') as file:
        toml.dump(toml_data, file)

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
    compile_commands = generate_compile_commands(regression_config, system_config)
    run_commands = generate_run_commands(regression_config, system_config)

    # Write Commands to TOML Files
    write_commands_to_toml(compile_commands, 'CompileCommands.toml')
    write_commands_to_toml(run_commands, 'RunCommands.toml')

    print("Compile and run commands, along with directories, have been generated and saved to TOML files.")
