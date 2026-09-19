"""
LeetCode CLI - Modular command-line interface
"""

from .i18n import t, set_language, get_language
from .input_utils import input_until_valid, input_pick_array
from .browser_cookie import get_browser_cookie, list_browser_cookies, read_cookie_from_file, HAS_BROWSER_COOKIE
from .cookie_manager import check_and_update_cookie
from .cookie_select import select_browser_cookie, candidate_label

__all__ = [
    't', 'set_language', 'get_language',
    'input_until_valid', 'input_pick_array',
    'get_browser_cookie', 'list_browser_cookies', 'read_cookie_from_file', 'HAS_BROWSER_COOKIE',
    'check_and_update_cookie',
    'select_browser_cookie', 'candidate_label',
]
