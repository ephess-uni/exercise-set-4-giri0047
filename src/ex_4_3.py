""" ex_4_3.py """

import os
from datetime import timedelta

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
    Calculate the time between the first and last shutdown events in the log file.

    :param logfile: The filename of the log file.
    :return: A timedelta representing the time between the first and last shutdown events.
    """
    shutdown_events = get_shutdown_events(logfile)
    if not shutdown_events:
        return timedelta()  # No shutdown events found, return a zero timedelta.

    # Convert the date fields to datetime objects
    shutdown_events = [logstamp_to_datetime(entry['date']) for entry in shutdown_events]

    # Sort the events by timestamp
    shutdown_events.sort()

    # Calculate the time difference between the first and last shutdown events
    time_difference = shutdown_events[-1] - shutdown_events[0]

    return time_difference

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
