""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

FILENAME = get_data_file_path('messages.log')

def get_shutdown_events(logfile):
    shutdown_lines = []
    with open(logfile, "r") as f:
        for line in f:
            if "Shutdown initiated" in line:
                shutdown_lines.append(line.strip())
    return shutdown_lines

if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
