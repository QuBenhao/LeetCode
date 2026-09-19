"""
Browser cookie detection for LeetCode CLI
Automatically detects LeetCode CN cookies from installed browsers.
"""

import glob
import os
import sqlite3
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Optional: browser_cookie3 for auto-detecting LeetCode cookie
try:
    import browser_cookie3
    HAS_BROWSER_COOKIE = True
except ImportError:
    HAS_BROWSER_COOKIE = False

# Root path for reading cookie file
_root_path = Path(__file__).parent.parent.parent.parent

_domain = 'leetcode.cn'

# browser_cookie3 only reads the FIRST Chromium profile it finds (Default),
# so a login living in any other profile is invisible to it. These user-data
# dirs let us sweep every profile ourselves and pass each store explicitly.
_CHROMIUM_USER_DATA = {
    'Chrome': {
        'darwin': '~/Library/Application Support/Google/Chrome',
        'linux': '~/.config/google-chrome',
        'win32': os.path.join(os.getenv('LOCALAPPDATA', ''), 'Google', 'Chrome', 'User Data'),
    },
    'Edge': {
        'darwin': '~/Library/Application Support/Microsoft Edge',
        'linux': '~/.config/microsoft-edge',
        'win32': os.path.join(os.getenv('LOCALAPPDATA', ''), 'Microsoft', 'Edge', 'User Data'),
    },
    'Chromium': {
        'darwin': '~/Library/Application Support/Chromium',
        'linux': '~/.config/chromium',
        'win32': os.path.join(os.getenv('LOCALAPPDATA', ''), 'Chromium', 'User Data'),
    },
}


def _platform_key() -> str:
    if sys.platform == 'darwin':
        return 'darwin'
    if sys.platform.startswith('win'):
        return 'win32'
    return 'linux'


def _profile_cookie_files(user_data_dir: str) -> List[str]:
    """Existing per-profile Cookies stores under a Chromium user-data dir.

    Default profile first, then numbered profiles. Modern Chromium keeps the
    DB either at <profile>/Cookies or <profile>/Network/Cookies depending on
    platform and version, so both variants are globbed.
    """
    base = os.path.expanduser(user_data_dir)
    patterns = (
        ('Default', 'Cookies'),
        ('Default', 'Network', 'Cookies'),
        ('Profile *', 'Cookies'),
        ('Profile *', 'Network', 'Cookies'),
    )
    files, seen = [], set()
    for parts in patterns:
        for path in sorted(glob.glob(os.path.join(base, *parts))):
            if path not in seen:
                seen.add(path)
                files.append(path)
    return files


def _profile_label(cookie_file: str) -> str:
    """Profile directory name of a Cookies store ('Default', 'Profile 4', ...)."""
    parts = Path(cookie_file).parts
    if len(parts) >= 3 and parts[-2] == 'Network':
        return parts[-3]
    return parts[-2]


def _extract_cookies(cj) -> Optional[Tuple[str, int]]:
    cookies = list(cj)
    if not cookies:
        return None
    return "; ".join(f"{c.name}={c.value}" for c in cookies), len(cookies)


def _probe(browser_func, **kwargs) -> Optional[Tuple[str, int]]:
    """Call a browser_cookie3 factory, tolerating missing/locked stores."""
    try:
        return _extract_cookies(browser_func(domain_name=_domain, **kwargs))
    except (PermissionError, FileNotFoundError, sqlite3.OperationalError,
            browser_cookie3.BrowserCookieError):
        # Browser not installed, cookie database locked, or permission denied
        return None


def _collect_candidates(browser_name: str, browser_func, chromium_family: bool,
                        platform: str) -> List[Tuple[str, str, int]]:
    """Every candidate store of one browser: its default store, then each profile."""
    candidates = []
    found = _probe(browser_func)
    if found:
        candidates.append((found[0], browser_name, found[1]))

    if not chromium_family:
        return candidates
    user_data = _CHROMIUM_USER_DATA[browser_name].get(platform)
    if not user_data:
        return candidates

    for cookie_file in _profile_cookie_files(user_data):
        found = _probe(browser_func, cookie_file=cookie_file)
        if found:
            profile = _profile_label(cookie_file)
            label = browser_name if profile == 'Default' else f"{browser_name} ({profile})"
            candidates.append((found[0], label, found[1]))

    return candidates


def list_browser_cookies() -> List[Tuple[str, str, int]]:
    """
    All LeetCode CN cookie candidates found on this machine.

    Browsers are tried in order (Chrome, Edge, Firefox, Chromium); Chromium-family
    browsers contribute one candidate per profile that holds leetcode.cn cookies.
    Duplicate stores (the same session read twice) are collapsed.

    Returns:
        List of (cookie_string, browser_label, cookie_count), possibly empty
    """
    if not HAS_BROWSER_COOKIE:
        return []

    plan = [
        ('Chrome', browser_cookie3.chrome, True),
        ('Edge', browser_cookie3.edge, True),
        ('Firefox', browser_cookie3.firefox, False),
        ('Chromium', browser_cookie3.chromium, True),
    ]
    platform = _platform_key()

    candidates, seen = [], set()
    for browser_name, browser_func, chromium_family in plan:
        for candidate in _collect_candidates(browser_name, browser_func, chromium_family, platform):
            if candidate[0] not in seen:
                seen.add(candidate[0])
                candidates.append(candidate)
    return candidates


def get_browser_cookie() -> Optional[Tuple[str, str, int]]:
    """
    Auto-detect LeetCode CN cookie from browser.

    Convenience wrapper around list_browser_cookies() for callers that do not
    care which account the cookie belongs to; use list_browser_cookies() plus
    select_browser_cookie() when the account matters.

    Returns:
        Tuple of (cookie_string, browser_name, cookie_count) or None if not found
    """
    candidates = list_browser_cookies()
    return candidates[0] if candidates else None


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
