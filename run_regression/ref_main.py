# main.py

import toml
import sys
from config import Config
from comp_run_q_arb_ex import CompRunQArbEx
from watchdogs import Watchdog
from artifact_run_q_arb_ex import ArtifactRunQArbEx

def main(regression_config_file, system_config_file, compile_commands_file, run_commands_file):
    try:
        regression_config = toml.load(regression_config_file)
        system_config = toml.load(system_config_file)
        compile_commands = toml.load(compile_commands_file)
        run_commands = toml.load(run_commands_file)

        config = Config(regression_config)
        config.fill_queues(compile_commands, run_commands)
        config.set_status_wait(config.compile_wait_queue)
        config.set_status_wait(config.test_wait_queue)

        comp_run_arb_ex = CompRunQArbEx(config, system_config)
        comp_run_arb_ex.set_makefile_path(system_config['script']['compile_makefile'])
        comp_run_arb_ex.set_max_concurrent_task(system_config['script']['concurrent_compile'])
        comp_run_arb_ex.set_wait_queue(config.compile_wait_queue)
        comp_run_arb_ex.set_run_queue(config.compile_run_queue)
        comp_run_arb_ex.set_done_queue(config.compile_done_queue)
        comp_run_arb_ex.set_name("CompRunQArbEx")

        watchdog = Watchdog(config, system_config)
        watchdog.set_wait_queue(config.compile_wait_queue)
        watchdog.set_run_queue(config.compile_run_queue)
        watchdog.set_done_queue(config.compile_done_queue)
        watchdog.set_name("Watchdog")
        watchdog.set_max_timeout(system_config['script']['max_timeout_compile'])
        watchdog.set_eot_mode('compile')

        # Start threads
        threads = [comp_run_arb_ex, watchdog]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print("Graceful Shutdown:")
        config.print_queue(config.compile_wait_queue, "Compile Wait")
        config.print_queue(config.compile_run_queue, "Compile Run")
        config.print_queue(config.compile_done_queue, "Compile Done")

    except ValueError as error:
        print(f"Error occurred in main: {error}")
        sys.exit(1)

if __name__ == "__main__":
    args = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
    main(args["-regression_config"], args["-system_config"], "CompileCommands.toml", "RunCommands.toml")
