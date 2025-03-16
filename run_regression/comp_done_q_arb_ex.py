# comp_run_q_arb_ex.py
import os
import shutil
import subprocess
import threading
import concurrent.futures
import psutil
from queues import SmartQ
import time
import random
from icecream import ic
from queue_utils import SmartQUtils
from db_utils import DBUtils  # Import DBUtils
import hashlib

class CompDoneQArbEx(threading.Thread, SmartQUtils, DBUtils):  # Inherit from DBUtils
    def __init__(self, config, system_config, set_completion_ev):
        threading.Thread.__init__(self)
        SmartQUtils.__init__(self)
        DBUtils.__init__(self)
        self.config = config
        self.system_config = system_config
        self._wait_queue = None
        self._run_queue = None
        self._done_queue = None
        self.set_completion_ev = set_completion_ev
        self.previous_process_info = {}

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_wait_queue(self, q):
        if isinstance(q, SmartQ):
            self._wait_queue = q

    def set_run_queue(self, q):
        if isinstance(q, SmartQ):
            self._run_queue = q

    def set_done_queue(self, q):
        if isinstance(q, SmartQ):
            self._done_queue = q

    def run_command(self, command, subdir):
        process = subprocess.Popen(command.split(), cwd=subdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process

    def check_process_status(self, process):
        return process.poll() is None  # Returns True if the process is still running

    def _update_process_info(self, entry):
        """update process_info of a given entry."""
        process_info = self.get_process_info(entry['pid'])
        if process_info is not None:
            for key in entry['process_info']:
                if key in process_info:
                    entry['process_info'][key] = process_info[key]

    def run(self):
        while not self.config.compile_eot:
            delay = random.uniform(0, 1)

            # If no tasks are in the run queue, sleep and try again.
            if self._run_queue.is_empty():
                time.sleep(delay)
                continue

            current_entry = self._run_queue.peek()
            if current_entry is None:
                continue

            pid = current_entry['pid']
            process = current_entry['process']

            # Update process info once per iteration.
            self._update_process_info(current_entry)

            if process.poll() is not None:
                # Process has finished; set its status based on return code.
                match process.returncode:
                    case 0:
                        current_entry['status'] = 'ok'
                    case _:
                        current_entry['status'] = 'error'
                        process_hash_tag = current_entry['command'] + current_entry['subdir']
                        process_dir = os.path.abspath(os.path.join(self.config.root_dir, current_entry['subdir']))
                        print("Full path to process directory:", process_dir)
                        hash_tag = self.compute_hash_tag(process_hash_tag)
                        error_entries = self.extract_compile_log_errors(process, process_dir)
                        result_array = self.attach_hash_tag_to_errors(error_entries, hash_tag)
                        for entry in result_array:
                            # Extract the first and second members
                            error_text_current = entry[0]  # List of error details
                            hash_tag_current = entry[1]    # Hash tag string
                            self._done_queue.update_error_data(self.config.get_sql_db_name(), error_text_current, hash_tag_current)
                            ic(error_text_current, hash_tag_current, error_entries, hash_tag_current)
                self.set_doneq_start_time(current_entry, time.time())
                self._run_queue.remove(current_entry)
                self._done_queue.put(current_entry)
            else:
                # Process is still running.
                time.sleep(delay)

            # Check if all expected processes are done.
            if self._done_queue.get_size() == self.config.get_number_of_compile_workers():
                if self.set_completion_ev:
                    self.set_completion_ev.set()
                self.config.compile_eot = True

    def get_process_info(self, pid):
        """Fetch and print process information safely."""
        try:
            if not psutil.pid_exists(pid):
                print(f"Process {pid} does not exist.")
                return None

            p = psutil.Process(pid)
            process_info = {
                "pid": p.pid,
                "memory_rss": p.memory_info().rss,  # Resident Set Size
                "memory_vms": p.memory_info().vms,  # Virtual Memory Size
                "memory_percent": p.memory_percent(),
                "cpu_percent": p.cpu_percent(interval=1.0),
                "cpu_times": p.cpu_times(),
                "cpu_num": p.cpu_num()
            }
            updated_info = {}
            previous_info = self.previous_process_info.get(pid, {})

            # Update process_info only if new element is greater than old one
            for key, value in process_info.items():
                if key in previous_info:
                    if value > previous_info[key]:
                        updated_info[key] = value
                    else:
                        updated_info[key] = previous_info[key]
                else:
                    updated_info[key] = value

            # Check if there's any difference between updated_info and previous_info
            if previous_info != updated_info:
                self.previous_process_info[pid] = updated_info
                return updated_info
            else:
                return None

        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist (NoSuchProcess).")
        except psutil.AccessDenied:
            print(f"Permission denied to access process {pid} (AccessDenied).")
        except psutil.ZombieProcess:
            print(f"Process {pid} is a zombie (ZombieProcess).")
        except Exception as e:
            print(f"Unexpected error accessing process {pid}: {e}")

    def extract_compile_log_errors(self, process, process_dir):
        """
        Extract error and warning lines from the compile log file.
        """
        compile_log_config = self.system_config.get('CompileLog', {})
        logfile_name = compile_log_config.get('logfile_name', 'verilator_comp.log')
        error_keywords = compile_log_config.get('error_keywords', ['Error', '%Error', 'ERROR'])
        error_line_depth = compile_log_config.get('error_line_depth', 3)

        error_entries = []
        if process.returncode != 0:
            log_file_path = os.path.join(process_dir, logfile_name)
            if os.path.exists(log_file_path):
                try:
                    with open(log_file_path, 'r') as f:
                        lines = f.readlines()
                    i = 0
                    while i < len(lines):
                        line = lines[i]
                        if any(keyword in line for keyword in error_keywords) or ('warning' in line.lower()):
                            # Ensure the snippet does not go out of bounds
                            if i < len(lines):
                                snippet_lines = lines[i:i+error_line_depth]
                                # Strip each line and collect into a list
                                snippet = [snippet_line.strip() for snippet_line in snippet_lines]
                                error_entries.append(snippet)
                            i += error_line_depth  # skip the extracted block
                        else:
                            i += 1
                except Exception as e:
                    print(f"Error reading log file {log_file_path}: {e}")
            else:
                print(f"Log file {log_file_path} not found.")
        else:
            print("Process did not complete successfully; skipping log extraction.")
        return error_entries

    def attach_hash_tag_to_errors(self, error_entries, hash_tag):
        """
        Attach a hash tag to each error snippet in the error_entries list.

        Args:
            error_entries (list): A list of error snippets, where each snippet is a list of strings.
            hash_tag (str): The hash tag to be appended to each error snippet.

        Returns:
            list: A list of entries where each entry is of the form [error_snippet, hash_tag].

        Example:
            error_entries = [
                ['%Error: top_sim_error.v:24:9: syntax error, unexpected $finish', 
                '24 |         $finish;', 
                '         ^~~~~~~'],
                ['%Error: top_sim_error.v:34:1: syntax error, unexpected ${pli-system}',
                '34 | $foo', 
                ' ^~~~'],
                ['%Error: Cannot continue',
                'Verilator exit code: 1',
                'COMPILE FAILED']
            ]
            hash_tag = 'some_hash'

            Returns:
                [
                    [['%Error: top_sim_error.v:24:9: syntax error, unexpected $finish', '24 |         $finish;', '         ^~~~~~~'], 'some_hash'],
                    [['%Error: top_sim_error.v:34:1: syntax error, unexpected ${pli-system}', '34 | $foo', ' ^~~~'], 'some_hash'],
                    [['%Error: Cannot continue', 'Verilator exit code: 1', 'COMPILE FAILED'], 'some_hash']
                ]
        """
        result = []
        for snippet in error_entries:
            result.append([snippet, hash_tag])
        return result