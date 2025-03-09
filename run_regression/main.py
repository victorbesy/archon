import toml
import sys
from config import Config
from comp_run_q_arb_ex import CompRunQArbEx
from comp_done_q_arb_ex import CompDoneQArbEx
from queue_manager import QManager
from queue_adviser import QAdviser
from watchdogs import Watchdog
from artifact_run_q_arb_ex import ArtifactRunQArbEx
import threading
from icecream  import ic

def main(regression_config_file, system_config_file, compile_commands_file, run_commands_file):
    try:
        regression_config = toml.load(regression_config_file)
        system_config = toml.load(system_config_file)
        compile_commands = toml.load(compile_commands_file)
        run_commands = toml.load(run_commands_file)

        config = Config(regression_config)
        config.compile_wait_queue.init_queue(compile_commands)
        config.compile_wait_queue.set_queue_default(approved='CompRunQMng',status='wait')

        
        config.set_number_of_compile_workers(config.compile_wait_queue.get_size())
        config.set_number_of_test_workers(config.test_wait_queue.get_size())
        
        output_dir = system_config['database']['output_dir']
        
        db_name = system_config['database']['db_name']
        db_path = f"{output_dir}/{db_name}"
        config.set_sql_db_name(db_path)
        config.initialize_db(db_path)

        csv_name = system_config['database']['csv_name']
        csv_path = f"{output_dir}/{csv_name}"
        config.set_csv_name(csv_path)

#############################
        comp_run_eot_event = threading.Event()
        comp_run_arb_ex = CompRunQArbEx(config, system_config,comp_run_eot_event) # comp_run_event - output
        comp_run_arb_ex.set_makefile_path(system_config['script']['compile_makefile'])
        comp_run_arb_ex.set_max_concurrent_task(system_config['script']['concurrent_compile'])
        comp_run_arb_ex.set_wait_queue(config.compile_wait_queue)
        comp_run_arb_ex.set_run_queue(config.compile_run_queue)
        comp_run_arb_ex.set_done_queue(config.compile_done_queue)
        comp_run_arb_ex.set_name("CompRunQArbEx")

        comp_done_eot_event = threading.Event()
        comp_done_arb_ex = CompDoneQArbEx(config, system_config,comp_done_eot_event)  # comp_done_event - output
        #comp_done_arb_ex.set_makefile_path(system_config['script']['compile_makefile'])
        #comp_done_arb_ex.set_max_concurrent_task(system_config['script']['concurrent_compile'])
        comp_done_arb_ex.set_wait_queue(config.compile_wait_queue)
        comp_done_arb_ex.set_run_queue(config.compile_run_queue)
        comp_done_arb_ex.set_done_queue(config.compile_done_queue)
        comp_done_arb_ex.set_name("CompDoneQArbEx")

        comp_run_mng = QManager(config, system_config,comp_done_eot_event) # comp_done_event - input
        comp_run_mng.set_wait_queue(config.compile_wait_queue)
        comp_run_mng.set_run_queue(config.compile_run_queue)
        comp_run_mng.set_done_queue(config.compile_done_queue)
        comp_run_mng.set_name("CompRunQMng")

        comp_queue_adv = QAdviser(config, system_config,comp_done_eot_event)
        comp_queue_adv.set_input_queue(config.comp_adv_req_queue)
        comp_queue_adv.set_output_queue(config.comp_adv_resp_queue)
        comp_queue_adv.set_name("CompQueueAdv")

        compile_watchdog_eot_event = threading.Event()
        compile_watchdog = Watchdog(config, system_config, compile_watchdog_eot_event)
        compile_watchdog.set_wait_queue(config.compile_wait_queue)
        compile_watchdog.set_run_queue(config.compile_run_queue)
        compile_watchdog.set_done_queue(config.compile_done_queue)
        compile_watchdog.set_name("CompileWatchdog")
        compile_watchdog.set_max_timeout(system_config['script']['max_timeout_compile'])
        compile_watchdog.set_eot_mode('compile')
#############################

        artifact_watchdog_eot_event = threading.Event()
        artifact_watchdog = Watchdog(config, system_config, artifact_watchdog_eot_event)
        artifact_watchdog.set_wait_queue(config.test_wait_queue)
        artifact_watchdog.set_run_queue(config.test_run_queue)
        artifact_watchdog.set_done_queue(config.test_done_queue)
        artifact_watchdog.set_name("ArtifactWatchdog")
        artifact_watchdog.set_max_timeout(system_config['script']['max_timeout_test'])
        artifact_watchdog.set_eot_mode('run')

        # Start threads
        threads = [ comp_run_arb_ex,
                    comp_done_arb_ex,
                    comp_run_mng,
                    comp_queue_adv,
                    compile_watchdog
                    #artifact_run_arb_ex,
                    #artifact_done_arb_ex,
                    ]

        for thread in threads:
            thread.start()

        comp_done_eot_event.wait()
        #TODO uncomments for artifact run
        #artifact_watchdog.start()

        for thread in threads:
            thread.join()
        #TODO uncomment for artifact runs
        #artifact_watchdog.join()

        if not compile_watchdog_eot_event.is_set() and not artifact_watchdog_eot_event.is_set():
            print("Graceful Shutdown:")
            config.compile_wait_queue.print_queue("Compile Wait:")
            config.compile_run_queue.print_queue("Compile Run:")
            config.compile_done_queue.print_queue("Compile Done:")
            if not (config.compile_run_queue.is_empty()):
                print("ERROR:  config.compile_run_queue is not empty")
            else:
                print("PASS:  config.compile_run_queue is empty")
            if (not config.compile_wait_queue.is_empty()):
                print("ERROR:  config.compile_wait_queue is not empty")
            else:
                print("PASS:  config.compile_wait_queue is empty") 
        #config.compile_done_queue.visualize_schedule()                 
        config.compile_done_queue.save_to_csv(config.get_csv_name())

        config.compile_done_queue.save_to_db(config.get_sql_db_name())
      

        print("End of Regression")

    except ValueError as error:
        print(f"Error occurred in main: {error}")
        sys.exit(1)

if __name__ == "__main__":
    required_args = ["-regression_config", "-system_config", "-compile_commands", "-run_commands"]
    args = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}

    missing_args = [arg for arg in required_args if arg not in args]

    if missing_args:
        print(f"Missing arguments: {', '.join(missing_args)}")
        print("Usage: python main.py -regression_config=<path> -system_config=<path> -compile_commands=<path> -run_commands=<path>")
        sys.exit(1)

    main(args["-regression_config"], args["-system_config"], args["-compile_commands"], args["-run_commands"])
