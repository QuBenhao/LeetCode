import functools
import json
import logging
from pathlib import Path

import pytz
import datetime
import sys
import time


def get_china_local_time():
    # get current time
    cur_time = time.time()

    # convert current time to datetime in UTC
    utc_time = datetime.datetime.fromtimestamp(cur_time, datetime.timezone.utc)

    # create the timezone object for UTC+8
    timezone = pytz.timezone('Asia/Shanghai')  # Shanghai is in UTC+8

    # convert utc_time to local timezone
    return utc_time.replace(tzinfo=pytz.utc).astimezone(timezone)


def get_china_daily_time():
    local_time = get_china_local_time()
    # apply the same logic to get the start of day in local timezone
    min_timestamp = local_time.replace(hour=0, minute=0, second=0, microsecond=0)

    # convert back to timestamp
    min_timestamp = min_timestamp.timestamp()
    return min_timestamp


def get_cur_weekday():
    local_time = get_china_local_time()
    return local_time.weekday()


def _load_data():
    root_path = Path(__file__).resolve().parent.parent.parent
    holidays_path = root_path / "data" / "holiday.json"
    if holidays_path.exists():
        with holidays_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def is_chinese_workday(dt: datetime.datetime) -> bool:
    if is_chinese_holiday(dt):
        return False
    data = _load_data()
    year_str = str(dt.year)
    if year_str in data:
        workdays = data[year_str].get("workdays", [])
        if dt.strftime("%Y%m%d") in workdays:
            return True
    return dt.weekday() < 5


def is_chinese_holiday(dt: datetime.datetime) -> bool:
    year_str = str(dt.year)
    data = _load_data()
    if year_str not in data:
        return False
    holidays = data[year_str].get("holidays", [])
    return dt.strftime("%Y%m%d") in holidays


def timeout(second: int = 3):
    def timeout_decorator(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):

            if sys.platform == "darwin" or sys.platform == "linux":
                import signal

                def handle_timeout(sig, frame):
                    raise TimeoutError('function [%s] timeout [%s seconds] exceeded! ' % (func.__name__, second))

                signal.signal(signal.SIGALRM, handle_timeout)
                signal.alarm(second)
                result = func(*args, **kwargs)
            else:
                from threading import Thread

                res = [TimeoutError('function [%s] timeout [%s seconds] exceeded! ' % (func.__name__, second))]

                def new_func():
                    try:
                        res[0] = func(*args, **kwargs)
                    except Exception as e:
                        res[0] = e

                t = Thread(target=new_func)
                t.daemon = True
                try:
                    t.start()
                    t.join(second)
                except Exception as e:
                    logging.error('error starting thread', exc_info=True)
                    raise e
                ret = res[0]
                if isinstance(ret, BaseException):
                    raise ret
                return ret
            return result

        return wrapper_timer

    return timeout_decorator
