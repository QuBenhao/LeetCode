import base64
import json
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
    Checks if a LeetCode cookie has expired by examining the LEETCODE_SESSION JWT.

    Parameters:
        cookie (str): The cookie string to check. Should contain LEETCODE_SESSION.

    Returns:
        bool: True if the cookie is expired or invalid; False otherwise.
    """
    if not cookie:
        return True

    # 查找 LEETCODE_SESSION
    session_match = re.search(r'LEETCODE_SESSION=([^;]+)', cookie)
    if not session_match:
        return True

    session_token = session_match.group(1)

    try:
        # JWT 格式: header.payload.signature
        parts = session_token.split('.')
        if len(parts) != 3:
            return True

        # 解码 payload (第二部分)
        payload = parts[1]
        # 补齐 base64 padding
        payload += '=' * (4 - len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        payload_data = json.loads(decoded)

        # 检查过期时间字段 (exp 或 expired_time_)
        exp = payload_data.get('exp') or payload_data.get('expired_time_')
        if not exp:
            return True

        # exp 是过期时间，如果当前时间大于 exp，则已过期
        return time.time() > exp

    except Exception:
        # 如果解析失败，回退到旧逻辑检查其他时间戳
        timestamp_pattern = r"(?<!\d)[\s,=]*([1-9]\d{9})[\s,=]*(?!\d)"
        match = re.findall(timestamp_pattern, cookie)
        if not match:
            return True
        max_timestamp = max(match)
        return time.time() - int(max_timestamp) >= COOKIE_EXPIRY_SECONDS
