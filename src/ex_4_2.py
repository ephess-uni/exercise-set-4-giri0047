# ex_4_2.py
from datetime import datetime

def logstamp_to_datetime(datestr):
    """
    Converts a date string in the format 'YYYY-MM-DDTHH:MM:SS' to a datetime object.

    Args:
        datestr (str): The date string to convert.

    Returns:
        datetime.datetime: A datetime object representing the input date and time.
    """
    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')

# The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
