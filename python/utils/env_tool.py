import re
import time


def get_default_folder(problem_category: str = None, paid_only: bool = False):
    if problem_category == "database":
        return "mysql"
    return "problems" if not paid_only else "premiums"

def check_cookie_expired(cookie: str) -> bool:
    # re find all timestamp like '1747799908' in cookie
    timestamp_pattern = r"(?<!\d)[\s,=]*([1-9]\d{9})[\s,=]*(?!\d)"
    match = re.findall(timestamp_pattern, cookie)
    if not match:
        return True
    max_timestamp = max(match)
    # check if the timestamp is less than 30 days
    return time.time() - int(max_timestamp) >= 30 * 24 * 60 * 60
