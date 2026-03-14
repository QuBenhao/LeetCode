"""
Browser cookie detection for LeetCode CLI
Automatically detects LeetCode CN cookies from installed browsers.
"""

import sqlite3
import sys
from pathlib import Path
from typing import Optional, Tuple

# Optional: browser_cookie3 for auto-detecting LeetCode cookie
try:
    import browser_cookie3
    HAS_BROWSER_COOKIE = True
except ImportError:
    HAS_BROWSER_COOKIE = False

# Root path for reading cookie file
_root_path = Path(__file__).parent.parent.parent.parent


def get_browser_cookie() -> Optional[Tuple[str, str, int]]:
    """
    Auto-detect LeetCode CN cookie from browser.

    Returns:
        Tuple of (cookie_string, browser_name, cookie_count) or None if not found
    """
    if not HAS_BROWSER_COOKIE:
        return None

    browsers = [
        ('Chrome', browser_cookie3.chrome),
        ('Edge', browser_cookie3.edge),
        ('Firefox', browser_cookie3.firefox),
        ('Chromium', browser_cookie3.chromium),
    ]

    for browser_name, browser_func in browsers:
        try:
            cj = browser_func(domain_name='leetcode.cn')
            cookies = list(cj)
            if cookies:
                cookie_parts = [f"{c.name}={c.value}" for c in cookies]
                return "; ".join(cookie_parts), browser_name, len(cookies)
        except (PermissionError, FileNotFoundError, sqlite3.OperationalError) as e:
            # Browser may not be installed, cookie database locked, or permission denied
            continue

    return None


def read_cookie_from_file() -> Optional[str]:
    """
    Read Cookie from file (solves terminal input length limit).

    Returns:
        Cookie string read from file, or None if file doesn't exist
    """
    # Try reading from temp file
    cookie_file = _root_path / ".cookie_tmp"
    if cookie_file.exists():
        try:
            cookie = cookie_file.read_text(encoding='utf-8').strip()
            if cookie:
                print(f"✓ 从 .cookie_tmp 读取到 Cookie")
                # Delete temp file after reading
                cookie_file.unlink()
                return cookie
        except (PermissionError, FileNotFoundError, UnicodeDecodeError) as e:
            # File may be locked, deleted by another process, or encoding issue
            pass

    # Hint user about file input option
    print("\n💡 提示: Cookie 较长时，可以保存到 .cookie_tmp 文件，脚本会自动读取")
    print("   或者使用管道输入: cat cookie.txt | python leetcode.py")
    return None
