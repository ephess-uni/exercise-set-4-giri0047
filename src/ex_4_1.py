""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path


FILENAME = get_data_file_path('messages.log')


def num_shutdowns(logfile):
    shutdown_events = get_shutdown_events(logfile)
    return len(shutdown_events)

if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
