""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Calculate the time duration between the first and last shutdowns in the log file.

    Args:
        logfile (str): The path to the log file.

    Returns:
        datetime.timedelta: The time duration between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)
    
    if len(shutdown_events) < 2:
        # If there are less than 2 shutdown events, return a zero timedelta.
        return timedelta(seconds=0)
    
    # Convert the date fields of the first and last shutdown events to datetime objects.
    first_shutdown_time = logstamp_to_datetime(shutdown_events[0]['date'])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1]['date'])
    
    # Calculate the time duration between the first and last shutdowns.
    time_duration = last_shutdown_time - first_shutdown_time
    
    return time_duration

# The code below will call your function and print the results
if __name__ == "__main__":
    from datetime import timedelta
    print(f'{time_between_shutdowns(FILENAME)=}')
