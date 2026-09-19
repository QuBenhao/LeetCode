"""
Cookie candidate selection for the LeetCode CLI.

A machine can hold several logged-in leetcode.cn sessions (one per browser
profile). This module identifies which account each candidate belongs to by
decoding the LEETCODE_SESSION JWT, then applies a graduated policy: a single
account is used silently, and the user is only asked when candidates really
hold different accounts.
"""

import os
from typing import List, Optional, Tuple

from python.constants import LEETCODE_USER
from python.utils import check_cookie_expired, get_session_identity

from .i18n import t
from .input_utils import input_until_valid

Candidate = Tuple[str, str, int]  # (cookie_string, browser_label, cookie_count)


def account_of(cookie: str) -> str:
    """LeetCode account (slug, else username) carried by a cookie, or '' when unknown."""
    identity = get_session_identity(cookie) or {}
    return identity.get('user_slug') or identity.get('username') or ''


def candidate_label(candidate: Candidate) -> str:
    """Display label for a candidate, with the account when it can be identified."""
    account = account_of(candidate[0])
    return f"{candidate[1]} @{account}" if account else candidate[1]


def _dedupe_by_account(candidates: List[Candidate]) -> List[Candidate]:
    """Collapse candidates holding the same account, preferring a usable session.

    When the same account appears in several profiles, the first (Default first)
    is kept unless it is expired and a later one is still valid — otherwise the
    wizard would report "expired" while a working session was available.

    Candidates whose account cannot be identified are kept as-is, since they
    cannot be proven to be the same session.
    """
    unique, index_by_key = [], {}
    for candidate in candidates:
        identity = get_session_identity(candidate[0]) or {}
        key = identity.get('user_id') or identity.get('user_slug') or identity.get('username')
        # Unidentifiable cookies stay distinct: key on the cookie itself.
        key = f"account:{key}" if key else f"cookie:{candidate[0]}"

        if key in index_by_key:
            kept = index_by_key[key]
            if check_cookie_expired(unique[kept][0]) and not check_cookie_expired(candidate[0]):
                unique[kept] = candidate
            continue

        index_by_key[key] = len(unique)
        unique.append(candidate)
    return unique


def _prompt_choice(candidates: List[Candidate]) -> Optional[Candidate]:
    """Numbered account picker. Returns the chosen candidate, or None for manual input."""
    options = []
    for index, candidate in enumerate(candidates, 1):
        state = t('cookie_account_expired') if check_cookie_expired(candidate[0]) \
            else t('cookie_account_valid')
        options.append(t(
            'cookie_account_option',
            index=index,
            user=account_of(candidate[0]) or t('cookie_account_unknown'),
            browser=candidate[1],
            count=candidate[2],
            state=state,
        ))
    options.append(t('cookie_account_manual'))
    print(t('cookie_account_multi', options='\n'.join(options)))

    def _valid(value: str) -> bool:
        return value == '' or (value.isdigit() and 0 <= int(value) <= len(candidates))

    picked = input_until_valid(
        t('cookie_account_pick', max=len(candidates)),
        _valid,
        t('cookie_account_invalid', max=len(candidates)),
    )
    if picked == '0':
        return None
    return candidates[int(picked) - 1 if picked else 0]


def select_browser_cookie(candidates: List[Candidate],
                          preferred_slug: Optional[str] = None) -> Optional[Candidate]:
    """
    Pick the cookie candidate to use.

    Policy:
      - no candidate            -> None
      - one distinct account    -> used silently
      - several, one matches    -> chosen automatically (preferred_slug, else
        the configured LEETCODE_USER)
      - several distinct ones   -> the user picks from a numbered list

    Parameters:
        candidates (list): Output of list_browser_cookies().
        preferred_slug (str): Account slug to prefer, defaults to LEETCODE_USER.

    Returns:
        The chosen (cookie_string, browser_label, cookie_count) tuple, or None
        when the user prefers to enter a cookie manually.
    """
    if not candidates:
        return None

    unique = _dedupe_by_account(candidates)
    if len(unique) == 1:
        return unique[0]

    preferred = preferred_slug if preferred_slug is not None else os.getenv(LEETCODE_USER, '')
    if preferred:
        for candidate in unique:
            if account_of(candidate[0]) == preferred:
                print(t('cookie_account_auto', user=preferred))
                return candidate

    return _prompt_choice(unique)
