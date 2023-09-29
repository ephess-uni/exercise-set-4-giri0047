""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Reads the specified log file and returns a list of lines where a shutdown was initiated.

    :param logfile: The path to the log file.
    :return: A list of lines where a shutdown was initiated.
    """
    shutdown_lines = []

    try:
        with open(logfile, 'r') as file:
            for line in file:
                if "Shutdown initiated" in line:
                    shutdown_lines.append(line.strip())

    except FileNotFoundError:
        print(f"File not found: {logfile}")
    
    return shutdown_lines

if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")

