import os
from datetime import datetime, timedelta

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
    Calculate the amount of time between the first and last shutdowns in a log file.

    Args:
    logfile (str): The filename of the log file.

    Returns:
    timedelta: The time duration between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)
    
    if not shutdown_events:
        return timedelta()  # Return a zero timedelta if there are no shutdown events.

    first_shutdown_time = logstamp_to_datetime(shutdown_events[0]['date'])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1]['date'])

    # Compute the time difference and ensure it's a positive value.
    time_difference = abs(last_shutdown_time - first_shutdown_time)

    return time_difference

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
