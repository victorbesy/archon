import sqlite3
import json
import hashlib
import os
import csv

class DBUtils:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def compute_hash_tag(self, input_string):
        """Compute a SHA256 hash tag from input_string."""
        hash_input = (input_string).encode('utf-8')
        return hashlib.sha256(hash_input).hexdigest()

    def append_json(self, old_json, new_val):
        """Helper to load a JSON array, append new_val, and dump back to JSON."""
        try:
            arr = json.loads(old_json) if old_json else []
        except Exception:
            arr = []
        arr.append(new_val)
        return json.dumps(arr)

    def update_error_data(self, db_path, error, hash_tag):
        """
        Update the 'error_data' table in the SQLite database at db_path.

        If a row with the same error exists:
            - Check the hash_tag column (stored as a JSON array).
            - If the provided hash_tag already exists, do nothing.
            - Otherwise, append the new hash_tag using the append_json helper.
        If no such row exists, insert a new row with the error and a JSON array containing hash_tag.

        Args:
            db_path (str): Path to the SQLite database.
            error (list or str): The error snippet (as a list of lines or a string) to be updated or inserted.
            hash_tag (str): The hash tag to be added.
        """
        # Ensure that error is a string (serialize it if it's a list)
        if isinstance(error, list):
            error_key = json.dumps(error)
        else:
            error_key = error

        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Ensure the error_data table exists
        c.execute("CREATE TABLE IF NOT EXISTS error_data (error TEXT PRIMARY KEY, hash_tag TEXT)")

        # Check if a row with the same error already exists
        c.execute("SELECT hash_tag FROM error_data WHERE error = ?", (error_key,))
        row = c.fetchone()

        if row is None:
            # No row exists for this error; insert a new row with the hash_tag stored as a JSON array
            hash_tag_json = json.dumps([hash_tag])
            c.execute("INSERT INTO error_data (error, hash_tag) VALUES (?, ?)", (error_key, hash_tag_json))
        else:
            # A row exists; load the existing JSON array of hash tags
            old_hash_json = row[0]
            try:
                hash_list = json.loads(old_hash_json) if old_hash_json else []
            except Exception:
                hash_list = []
            # Append the new hash_tag if not already present
            if hash_tag not in hash_list:
                new_hash_json = self.append_json(old_hash_json, hash_tag)
                c.execute("UPDATE error_data SET hash_tag = ? WHERE error = ?", (new_hash_json, error_key))
            # Else, the hash_tag already exists; do nothing

        conn.commit()
        conn.close()

    def update_queue_data(self, db_path, item):
        """
        Update a single row in the queue_data table of the SQLite database.

        Args:
            c (sqlite3.Cursor): The SQLite cursor object.
            item (dict): The item to be updated in the database.
        """
        # Connect to the SQLite database.
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Create queue_data table if it doesn't exist (safety check; normally the db is already initialized).
        create_table_query = """
        CREATE TABLE IF NOT EXISTS queue_data (
            hash_tag TEXT,
            command TEXT,
            subdir TEXT,
            status TEXT,
            memory_rss TEXT,
            memory_vms TEXT,
            memory_percent TEXT,
            cpu_percent TEXT,
            cpu_num TEXT,
            cpu_times_user TEXT,
            cpu_times_system TEXT,
            cpu_times_children_user TEXT,
            cpu_times_children_system TEXT,
            cpu_times_iowait TEXT,
            adviser_response_get_worker_info TEXT,
            adviser_response_worker_resource_config TEXT,
            adviser_response_change_worker TEXT,
            wait_time TEXT,
            run_time TEXT,
            total_time TEXT,
            PRIMARY KEY (command, subdir)
        );
        """
        c.execute(create_table_query)
        conn.commit()

        command = item['command']
        subdir = item['subdir']
        status_val = item['status']

        # Compute the hash_tag using the class method.
        hash_id = command + subdir
        hash_tag = self.compute_hash_tag(hash_id)

        process_info = item['process_info']
        # Extract original timestamps.
        waitq_start = process_info.get('waitq_start_time', 0)
        runq_start = process_info.get('runq_start_time', 0)
        doneq_start = process_info.get('doneq_start_time', 0)

        # Calculate new time columns.
        wait_time = runq_start - waitq_start
        run_time = doneq_start - runq_start
        total_time = doneq_start - waitq_start

        # Extract process_info values.
        memory_rss = process_info.get('memory_rss', 0)
        memory_vms = process_info.get('memory_vms', 0)
        memory_percent = process_info.get('memory_percent', 0)
        cpu_percent = process_info.get('cpu_percent', 0)
        cpu_num = process_info.get('cpu_num', 0)

        # Extract CPU times safely.
        cpu_times = process_info.get('cpu_times', None)
        if cpu_times is None:
            cpu_times_user = cpu_times_system = cpu_times_children_user = cpu_times_children_system = cpu_times_iowait = 0
        elif isinstance(cpu_times, dict):
            cpu_times_user = cpu_times.get('user', 0)
            cpu_times_system = cpu_times.get('system', 0)
            cpu_times_children_user = cpu_times.get('children_user', 0)
            cpu_times_children_system = cpu_times.get('children_system', 0)
            cpu_times_iowait = cpu_times.get('iowait', 0)
        else:
            cpu_times_user = getattr(cpu_times, 'user', 0)
            cpu_times_system = getattr(cpu_times, 'system', 0)
            cpu_times_children_user = getattr(cpu_times, 'children_user', 0)
            cpu_times_children_system = getattr(cpu_times, 'children_system', 0)
            cpu_times_iowait = getattr(cpu_times, 'iowait', 0)

        # Extract adviser_response values.
        adviser_response = item['adviser_response']
        get_worker_info = adviser_response.get('get_worker_info', 'NA')
        worker_resource_config = adviser_response.get('worker_resource_config', 'NA')
        change_worker = adviser_response.get('change_worker', 'NA')

        # Check if a row with the same (command, subdir) already exists.
        c.execute(
            """SELECT status, memory_rss, memory_vms, memory_percent, cpu_percent, cpu_num,
                    cpu_times_user, cpu_times_system, cpu_times_children_user, cpu_times_children_system,
                    cpu_times_iowait, adviser_response_get_worker_info, adviser_response_worker_resource_config,
                    adviser_response_change_worker, wait_time, run_time, total_time
            FROM queue_data 
            WHERE command=? AND subdir=?""",
            (command, subdir)
        )
        row = c.fetchone()

        if row is None:
            # Insert a new row with each column stored as a JSON array (with one element).
            insert_query = """
                INSERT INTO queue_data (
                    hash_tag, command, subdir, status, memory_rss, memory_vms, memory_percent,
                    cpu_percent, cpu_num, cpu_times_user, cpu_times_system, cpu_times_children_user,
                    cpu_times_children_system, cpu_times_iowait, adviser_response_get_worker_info,
                    adviser_response_worker_resource_config, adviser_response_change_worker,
                    wait_time, run_time, total_time
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            data = (
                hash_tag,
                command,
                subdir,
                json.dumps([status_val]),
                json.dumps([memory_rss]),
                json.dumps([memory_vms]),
                json.dumps([memory_percent]),
                json.dumps([cpu_percent]),
                json.dumps([cpu_num]),
                json.dumps([cpu_times_user]),
                json.dumps([cpu_times_system]),
                json.dumps([cpu_times_children_user]),
                json.dumps([cpu_times_children_system]),
                json.dumps([cpu_times_iowait]),
                json.dumps([get_worker_info]),
                json.dumps([worker_resource_config]),
                json.dumps([change_worker]),
                json.dumps([wait_time]),
                json.dumps([run_time]),
                json.dumps([total_time])
            )
            c.execute(insert_query, data)
        else:
            (old_status, old_memory_rss, old_memory_vms, old_memory_percent, old_cpu_percent, old_cpu_num,
            old_cpu_times_user, old_cpu_times_system, old_cpu_times_children_user, old_cpu_times_children_system,
            old_cpu_times_iowait, old_get_worker_info, old_worker_resource_config, old_change_worker,
            old_wait_time, old_run_time, old_total_time) = row

            update_query = """
                UPDATE queue_data SET
                    status = ?,
                    memory_rss = ?,
                    memory_vms = ?,
                    memory_percent = ?,
                    cpu_percent = ?,
                    cpu_num = ?,
                    cpu_times_user = ?,
                    cpu_times_system = ?,
                    cpu_times_children_user = ?,
                    cpu_times_children_system = ?,
                    cpu_times_iowait = ?,
                    adviser_response_get_worker_info = ?,
                    adviser_response_worker_resource_config = ?,
                    adviser_response_change_worker = ?,
                    wait_time = ?,
                    run_time = ?,
                    total_time = ?
                WHERE command = ? AND subdir = ?
            """
            new_values = (
                self.append_json(old_status, status_val),
                self.append_json(old_memory_rss, memory_rss),
                self.append_json(old_memory_vms, memory_vms),
                self.append_json(old_memory_percent, memory_percent),
                self.append_json(old_cpu_percent, cpu_percent),
                self.append_json(old_cpu_num, cpu_num),
                self.append_json(old_cpu_times_user, cpu_times_user),
                self.append_json(old_cpu_times_system, cpu_times_system),
                self.append_json(old_cpu_times_children_user, cpu_times_children_user),
                self.append_json(old_cpu_times_children_system, cpu_times_children_system),
                self.append_json(old_cpu_times_iowait, cpu_times_iowait),
                self.append_json(old_get_worker_info, get_worker_info),
                self.append_json(old_worker_resource_config, worker_resource_config),
                self.append_json(old_change_worker, change_worker),
                self.append_json(old_wait_time, wait_time),
                self.append_json(old_run_time, run_time),
                self.append_json(old_total_time, total_time),
                command,
                subdir
            )
            c.execute(update_query, new_values) 

        conn.commit()
        conn.close()

    def initialize_db(self, db_path):
        """
        Initialize the SQLite database at db_path if it does not already exist.
        
        If the database file exists, do nothing.
        Otherwise, create the database with two tables:
        1. queue_data, with the following columns:
                hash_tag TEXT,
                command TEXT,
                subdir TEXT,
                status TEXT,
                memory_rss TEXT,
                memory_vms TEXT,
                memory_percent TEXT,
                cpu_percent TEXT,
                cpu_num TEXT,
                cpu_times_user TEXT,
                cpu_times_system TEXT,
                cpu_times_children_user TEXT,
                cpu_times_children_system TEXT,
                cpu_times_iowait TEXT,
                adviser_response_get_worker_info TEXT,
                adviser_response_worker_resource_config TEXT,
                adviser_response_change_worker TEXT,
                wait_time TEXT,
                run_time TEXT,
                total_time TEXT,
            and a primary key on (command, subdir).
        
        2. error_data, with the following columns:
                error TEXT PRIMARY KEY,
                hash_tag TEXT
            This table is initialized with two rows:
                ("Error", "Error") and ("hash_tag", "hash_tag").
        """
        if os.path.exists(db_path):
            return

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Create the queue_data table.
        create_queue_query = """
        CREATE TABLE IF NOT EXISTS queue_data (
            hash_tag TEXT,
            command TEXT,
            subdir TEXT,
            status TEXT,
            memory_rss TEXT,
            memory_vms TEXT,
            memory_percent TEXT,
            cpu_percent TEXT,
            cpu_num TEXT,
            cpu_times_user TEXT,
            cpu_times_system TEXT,
            cpu_times_children_user TEXT,
            cpu_times_children_system TEXT,
            cpu_times_iowait TEXT,
            adviser_response_get_worker_info TEXT,
            adviser_response_worker_resource_config TEXT,
            adviser_response_change_worker TEXT,
            wait_time TEXT,
            run_time TEXT,
            total_time TEXT,
            PRIMARY KEY (command, subdir)
        );
        """
        c.execute(create_queue_query)

        # Create the error_data table.
        create_error_query = """
        CREATE TABLE IF NOT EXISTS error_data (
            error TEXT PRIMARY KEY,
            hash_tag TEXT
        );
        """
        c.execute(create_error_query)

        conn.commit()
        conn.close()
    def save_to_csv(self, filepath):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Define the main header
            header_main = [
                'command', 'subdir', 'status', 'approved', 'adviser', 'process', 'process_info',
                'process_info', 'process_info', 'process_info', 'process_info', 'process_info', 'process_info',
                'process_info', 'process_info', 'process_info', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times',
                'adviser_response', 'adviser_response', 'adviser_response', 'pid'
            ]
            
            # Define the sub-header
            header_sub = ['', '', '', '', '', '', 'pid', 'memory', 'memory', 'memory', 'cpu', 'cpu', '', '', '',
                          'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', 'cpu_times', '', '', '', '']
            
            # Define the third header row
            header_third = ['', '', '', '', '', '', '', 'rss', 'vms', 'percent', 'percent', 'num', 'waitq_start_time', 'runq_start_time', 'doneq_start_time',
                            'user', 'system', 'children_user', 'children_system', 'iowait', 'get_worker_info', 'worker_resource_config', 'change_worker', '']
            
            # Write header rows
            writer.writerow(header_main)
            writer.writerow(header_sub)
            writer.writerow(header_third)
            
            # Write data rows
            for item in self:
                process_info = item['process_info']
                adviser_response = item['adviser_response']
                row = [
                    item['command'],
                    item['subdir'],
                    item['status'],
                    ','.join(item['approved']) if isinstance(item['approved'], list) else item['approved'],
                    item['adviser'],
                    str(item['process']),
                    process_info.get('pid', 0)
                ]
                # Append process_info values
                row.extend([
                    process_info.get('memory_rss', 0),
                    process_info.get('memory_vms', 0),
                    process_info.get('memory_percent', 0),
                    process_info.get('cpu_percent', 0),
                    process_info.get('cpu_num', 0),
                    process_info.get('waitq_start_time', 0),
                    process_info.get('runq_start_time', 0),
                    process_info.get('doneq_start_time', 0)
                ])
                # Append cpu_times values
                cpu_times = process_info.get('cpu_times', {})
                row.extend([getattr(cpu_times, key, 0) for key in ['user', 'system', 'children_user', 'children_system', 'iowait']])
                # Append adviser_response values
                row.extend([adviser_response.get(key, 'NA') for key in ['get_worker_info', 'worker_resource_config', 'change_worker']])
                # Append final pid column
                row.append(item.get('pid', 0))
                writer.writerow(row)
        
        if self.verbose:
            print(f"Queue information saved to {filepath}")    