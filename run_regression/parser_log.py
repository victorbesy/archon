import sys

# Define the error keywords here
ERROR_KEYWORDS = ["error", "warning", "fatal","exception","traceback","Timeout reached"]

def parse_log_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                for keyword in ERROR_KEYWORDS:
                    if (keyword.islower() and keyword in line.lower()) or (not keyword.islower() and keyword in line):
                        print(f"Error found in log file: {line.strip()}")
                        sys.exit(1)  # Exit with error code 1
        print("Test passed")
        sys.exit(0)  # Exit with success code 0
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(2)  # Exit with error code 2 for file not found
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(3)  # Exit with error code 3 for other exceptions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser_log.py <log_file>")
        sys.exit(4)  # Exit with error code 4 for incorrect usage

    log_file = sys.argv[1]
    parse_log_file(log_file)
