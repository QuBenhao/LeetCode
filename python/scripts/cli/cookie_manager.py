"""
Cookie management for LeetCode CLI
Handles cookie validation, update, and refresh workflows.
"""

from typing import Optional

from python.utils import check_cookie_expired

from .i18n import t
from .input_utils import input_until_valid, allow_all, allow_all_not_empty
from .browser_cookie import get_browser_cookie, read_cookie_from_file, HAS_BROWSER_COOKIE

SEPARATE_LINE = "-" * 50


def check_and_update_cookie(_cookie: str, auto_detect: bool = True) -> str:
    """
    Check cookie validity and prompt for update if needed.

    Args:
        _cookie: Current cookie string
        auto_detect: Whether to try auto-detecting from browser

    Returns:
        Updated cookie string (may be same as input if valid)
    """
    while check_cookie_expired(_cookie):
        print(t("cookie_expired"))

        # Try auto-detect from browser
        if auto_detect and HAS_BROWSER_COOKIE:
            auto_detect_choice = input_until_valid(
                t("cookie_auto_detect"),
                allow_all
            )
            if auto_detect_choice != "n":
                print(t("cookie_detecting"))
                result = get_browser_cookie()
                if result:
                    cookie, browser_name, cookie_count = result
                    print(t("cookie_detected", browser=browser_name, count=cookie_count))
                    # Verify the new cookie
                    if not check_cookie_expired(cookie):
                        print(t("cookie_verified"))
                        return cookie
                    else:
                        print(t("cookie_auto_invalid"))
                        print(t("init_no_cookie_hint"))
                else:
                    print(t("init_no_cookie"))
                    print(t("init_no_cookie_hint"))

        # Try reading from file
        file_cookie = read_cookie_from_file()
        if file_cookie and not check_cookie_expired(file_cookie):
            print(t("cookie_verified"))
            return file_cookie

        # Manual input
        update_cookie = input_until_valid(
            t("cookie_manual"),
            allow_all
        )
        if update_cookie == "y":
            print("\n💡 Cookie 较长时，建议保存到 .cookie_tmp 文件后重试")
            _cookie = input_until_valid(
                t("init_enter_cookie"),
                allow_all_not_empty,
                t("init_cookie_empty")
            )
            print(t("config_cookie_updated"))
        else:
            print(t("cookie_continue"))
            break
        print(SEPARATE_LINE)
    return _cookie
