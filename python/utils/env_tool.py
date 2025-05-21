import re
import time
from typing import Optional

from python.constants import COOKIE_EXPIRY_SECONDS


def get_default_folder(problem_category: str = None, paid_only: bool = False):
    if problem_category == "database":
        return "mysql"
    return "problems" if not paid_only else "premiums"

def check_cookie_expired(cookie: Optional[str]) -> bool:
    """
    Checks if a cookie has expired based on timestamps found within it.

    Parameters:
        cookie (str): The cookie string to check. It is expected to contain one or more
        Unix timestamps in seconds (e.g., '1747799908') embedded within the string.

    Returns:
        bool: True if the cookie is expired or if no valid timestamps are found;
        False otherwise.

    Edge Cases:
        - If the cookie string is empty or does not contain any valid timestamps,
          the function will return True (indicating the cookie is expired).
        - Malformed cookies with non-numeric or invalid timestamp formats are ignored.
    """
    if not cookie:
        return True
    # re find all timestamp like '1747799908' in cookie
    timestamp_pattern = r"(?<!\d)[\s,=]*([1-9]\d{9})[\s,=]*(?!\d)"
    match = re.findall(timestamp_pattern, cookie)
    if not match:
        return True
    max_timestamp = max(match)
    # check if the timestamp is less than 30 days
    return time.time() - int(max_timestamp) >= COOKIE_EXPIRY_SECONDS
