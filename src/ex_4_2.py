""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    try:
      
        return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
       
        return datetime.strptime(datestr + '.000000', '%Y-%m-%dT%H:%M:%S.%f')


if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
