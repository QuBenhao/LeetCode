import pytz
from datetime import datetime
import time


def get_china_daily_time():
    # get current time
    cur_time = time.time()

    # convert current time to datetime in UTC
    utc_time = datetime.utcfromtimestamp(cur_time)

    # create the timezone object for UTC+8
    timezone = pytz.timezone('Asia/Shanghai')  # Shanghai is in UTC+8

    # convert utc_time to local timezone
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(timezone)

    # apply the same logic to get the start of day in local timezone
    min_timestamp = local_time.replace(hour=0, minute=0, second=0, microsecond=0)

    # convert back to timestamp
    min_timestamp = min_timestamp.timestamp()
    return min_timestamp
