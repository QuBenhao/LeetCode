"""Tests for browser cookie detection, session identity, and account selection."""

import base64
import json
import re
import sqlite3
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pytest

from python.constants import COOKIE_EXPIRY_SECONDS
from python.scripts.cli import browser_cookie
from python.scripts.cli.cookie_select import (
    account_of,
    candidate_label,
    select_browser_cookie,
)
from python.scripts.cli.i18n import I18N
from python.utils import check_cookie_expired, get_session_identity


def _jwt(payload: Any) -> str:
    def _b64(data: Any) -> str:
        raw = json.dumps(data).encode('utf-8')
        return base64.urlsafe_b64encode(raw).decode('utf-8').rstrip('=')

    return f"{_b64({'alg': 'HS256'})}.{_b64(payload)}.signature"


def _session_cookie(payload: Any, *, prefix: str = "") -> str:
    return f"{prefix}LEETCODE_SESSION={_jwt(payload)}; csrftoken=abc"


class _FakeCookie:
    def __init__(self, name: str, value: str):
        self.name, self.value = name, value


# --------------------------------------------------------------------------- #
# check_cookie_expired refactor equivalence
# --------------------------------------------------------------------------- #

def _legacy_check_cookie_expired(cookie):
    """Pre-refactor implementation, kept here as the behaviour contract."""
    if not cookie:
        return True

    session_match = re.search(r'LEETCODE_SESSION=([^;]+)', cookie)
    if not session_match:
        return True

    session_token = session_match.group(1)

    try:
        parts = session_token.split('.')
        if len(parts) != 3:
            return True

        payload = parts[1]
        payload += '=' * (4 - len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        payload_data = json.loads(decoded)

        exp = payload_data.get('exp') or payload_data.get('expired_time_')
        if not exp:
            return True

        return time.time() > exp

    except Exception:
        timestamp_pattern = r"(?<!\d)[\s,=]*([1-9]\d{9})[\s,=]*(?!\d)"
        match = re.findall(timestamp_pattern, cookie)
        if not match:
            return True
        max_timestamp = max(match)
        return time.time() - int(max_timestamp) >= COOKIE_EXPIRY_SECONDS


def _cookie_samples() -> List[Tuple[str, str]]:
    now = int(time.time())
    return [
        ("empty", ""),
        ("no session cookie", "csrftoken=abc; _gid=xyz"),
        ("one part token", "LEETCODE_SESSION=notajwt"),
        ("two part token", "LEETCODE_SESSION=aaa.bbb"),
        ("undecodable payload", "LEETCODE_SESSION=aaa.@@@.ccc"),
        ("undecodable payload with old stamp", f"LEETCODE_SESSION=aaa.@@@.ccc; t={now - COOKIE_EXPIRY_SECONDS - 60}"),
        ("undecodable payload with fresh stamp", f"LEETCODE_SESSION=aaa.@@@.ccc; t={now - 10}"),
        ("valid unexpired", _session_cookie({"exp": now + 3600, "username": "alice"})),
        ("valid expired", _session_cookie({"exp": now - 3600, "username": "alice"})),
        ("expired_time_ field", _session_cookie({"expired_time_": now - 3600})),
        ("no expiry field", _session_cookie({"username": "alice"})),
        ("non-dict payload", _session_cookie([1, 2, 3])),
        ("string expiry", _session_cookie({"exp": str(now + 3600)})),
        ("null expiry", _session_cookie({"exp": None, "username": "alice"})),
    ]


@pytest.mark.unit
@pytest.mark.parametrize("label,cookie", _cookie_samples(), ids=lambda v: v if isinstance(v, str) and len(v) < 40 else "")
def test_cookie_expiry_matches_legacy_behaviour(label: str, cookie: str):
    assert check_cookie_expired(cookie) == _legacy_check_cookie_expired(cookie)


@pytest.mark.unit
def test_cookie_expiry_recognises_valid_and_expired_sessions():
    now = int(time.time())
    assert check_cookie_expired(_session_cookie({"exp": now + 3600})) is False
    assert check_cookie_expired(_session_cookie({"exp": now - 3600})) is True


# --------------------------------------------------------------------------- #
# Session identity
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_session_identity_reads_account_from_jwt():
    cookie = _session_cookie({"user_slug": "benhao", "username": "benhao", "id": 4242})

    assert get_session_identity(cookie) == {
        'user_slug': 'benhao',
        'username': 'benhao',
        'user_id': 4242,
    }


@pytest.mark.unit
def test_session_identity_falls_back_to_username_when_slug_missing():
    assert account_of(_session_cookie({"username": "alice"})) == "alice"


@pytest.mark.unit
@pytest.mark.parametrize("cookie", ["", "csrftoken=abc", "LEETCODE_SESSION=notajwt",
                                    "LEETCODE_SESSION=aaa.@@@.ccc", _session_cookie([1, 2])])
def test_session_identity_absent_for_unusable_cookies(cookie: str):
    assert get_session_identity(cookie) is None
    assert account_of(cookie) == ""


# --------------------------------------------------------------------------- #
# Account selection policy
# --------------------------------------------------------------------------- #

def _candidate(slug: str, label: str) -> Tuple[str, str, int]:
    return _session_cookie({"user_slug": slug, "username": slug, "id": slug,
                            "exp": int(time.time()) + 3600}), label, 19


@pytest.mark.unit
def test_selection_is_silent_for_single_account(monkeypatch):
    def _fail(_prompt: str = "") -> str:
        pytest.fail("single account must not prompt")

    monkeypatch.setattr('builtins.input', _fail)
    candidates = [_candidate('alice', 'Chrome')]

    assert select_browser_cookie(candidates) == candidates[0]


@pytest.mark.unit
def test_selection_dedupes_same_account_across_profiles(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _prompt="": pytest.fail("same account must not prompt"))
    first = _candidate('alice', 'Chrome')
    second = _candidate('alice', 'Chrome (Profile 4)')

    assert select_browser_cookie([first, second]) == first


@pytest.mark.unit
def test_selection_prefers_valid_session_when_same_account_is_duplicated(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _prompt="": pytest.fail("same account must not prompt"))
    now = int(time.time())
    stale = (_session_cookie({"user_slug": "alice", "username": "alice", "id": "alice",
                              "exp": now - 3600}), 'Chrome', 19)
    fresh = (_session_cookie({"user_slug": "alice", "username": "alice", "id": "alice",
                              "exp": now + 3600}), 'Chrome (Profile 4)', 19)

    assert select_browser_cookie([stale, fresh]) == fresh
    # order of discovery must not matter
    assert select_browser_cookie([fresh, stale]) == fresh


@pytest.mark.unit
def test_selection_prefers_configured_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _prompt="": pytest.fail("matched account must not prompt"))
    alice = _candidate('alice', 'Chrome')
    bob = _candidate('bob', 'Chrome (Profile 4)')

    assert select_browser_cookie([alice, bob], preferred_slug='bob') == bob


@pytest.mark.unit
def test_selection_reads_configured_user_from_env(monkeypatch):
    monkeypatch.setenv('LEETCODE_USER', 'benhao')
    monkeypatch.setattr('builtins.input', lambda _prompt="": pytest.fail("matched account must not prompt"))
    other = _candidate('alice', 'Chrome')
    mine = _candidate('benhao', 'Chrome (Profile 1)')

    assert select_browser_cookie([other, mine]) == mine


@pytest.mark.unit
def test_selection_asks_when_accounts_differ(monkeypatch, capsys):
    alice = _candidate('alice', 'Chrome')
    bob = _candidate('bob', 'Chrome (Profile 4)')
    monkeypatch.setattr('builtins.input', lambda _prompt="": "2")

    assert select_browser_cookie([alice, bob], preferred_slug='') == bob

    output = capsys.readouterr().out
    assert 'alice' in output and 'bob' in output


@pytest.mark.unit
def test_selection_allows_manual_entry(monkeypatch):
    alice = _candidate('alice', 'Chrome')
    bob = _candidate('bob', 'Chrome (Profile 4)')
    monkeypatch.setattr('builtins.input', lambda _prompt="": "0")

    assert select_browser_cookie([alice, bob], preferred_slug='') is None


@pytest.mark.unit
def test_selection_retries_invalid_choice(monkeypatch):
    alice = _candidate('alice', 'Chrome')
    bob = _candidate('bob', 'Chrome (Profile 4)')
    answers = iter(["9", "bogus", ""])
    prompts = []

    def _fake_input(prompt: str = "") -> str:
        prompts.append(prompt)
        return next(answers)

    monkeypatch.setattr('builtins.input', _fake_input)

    # invalid inputs are rejected, empty input accepts the default (first account)
    assert select_browser_cookie([alice, bob], preferred_slug='') == alice
    assert len(prompts) == 3


@pytest.mark.unit
def test_selection_returns_none_without_candidates():
    assert select_browser_cookie([]) is None


@pytest.mark.unit
def test_candidate_label_includes_account_when_known():
    assert candidate_label(_candidate('alice', 'Chrome (Profile 4)')) == 'Chrome (Profile 4) @alice'
    assert candidate_label(("LEETCODE_SESSION=notajwt", "Chrome", 2)) == 'Chrome'


# --------------------------------------------------------------------------- #
# Candidate enumeration across profiles
# --------------------------------------------------------------------------- #

@pytest.fixture
def chrome_stores(tmp_path: Path, monkeypatch):
    """Fake Chrome user-data dir with Default + two profile stores."""
    user_data = tmp_path / "Chrome"
    for profile in ("Default", "Profile 4", "Profile 5"):
        store = user_data / profile / "Cookies"
        store.parent.mkdir(parents=True, exist_ok=True)
        store.write_text("", encoding="utf-8")
    monkeypatch.setitem(browser_cookie._CHROMIUM_USER_DATA['Chrome'],
                        browser_cookie._platform_key(), str(user_data))
    return user_data


def _install_fake_browsers(monkeypatch, chrome):
    monkeypatch.setattr(browser_cookie.browser_cookie3, 'chrome', chrome)
    for name in ('edge', 'firefox', 'chromium'):
        monkeypatch.setattr(
            browser_cookie.browser_cookie3, name,
            lambda **kwargs: (_ for _ in ()).throw(
                browser_cookie.browser_cookie3.BrowserCookieError(f"no {name}")))


@pytest.mark.unit
def test_list_browser_cookies_collects_every_profile(chrome_stores, monkeypatch):
    def fake_chrome(cookie_file=None, domain_name="", key_file=None):
        if cookie_file and cookie_file.endswith("Profile 4/Cookies"):
            return [_FakeCookie("LEETCODE_SESSION", "profile4")]
        return []

    _install_fake_browsers(monkeypatch, fake_chrome)

    candidates = browser_cookie.list_browser_cookies()

    assert [label for _, label, _ in candidates] == ['Chrome (Profile 4)']
    assert browser_cookie.get_browser_cookie() == candidates[0]


@pytest.mark.unit
def test_list_browser_cookies_keeps_default_first_and_dedupes(chrome_stores, monkeypatch):
    def fake_chrome(cookie_file=None, domain_name="", key_file=None):
        # Default is readable both through the default lookup and the profile sweep
        if cookie_file is None and False:
            return []
        return [_FakeCookie("LEETCODE_SESSION", "same-session")]

    _install_fake_browsers(monkeypatch, fake_chrome)

    candidates = browser_cookie.list_browser_cookies()

    assert len(candidates) == 1
    assert candidates[0][1] == 'Chrome'


@pytest.mark.unit
def test_list_browser_cookies_survives_browsers_without_stores(chrome_stores, monkeypatch):
    def fake_chrome(cookie_file=None, domain_name="", key_file=None):
        raise browser_cookie.browser_cookie3.BrowserCookieError("no Chrome")

    _install_fake_browsers(monkeypatch, fake_chrome)

    assert browser_cookie.list_browser_cookies() == []
    assert browser_cookie.get_browser_cookie() is None


@pytest.mark.unit
def test_detection_reports_permission_denial_instead_of_missing_store(chrome_stores, monkeypatch, capsys):
    def deny_directory_access(_path):
        raise PermissionError("private diagnostic text")

    def unexpected_cookie_read(**kwargs):
        pytest.fail("must not read cookies after directory access was denied")

    _install_fake_browsers(monkeypatch, unexpected_cookie_read)
    monkeypatch.setattr(browser_cookie.os, 'scandir', deny_directory_access)

    assert browser_cookie.detect_browser_cookies() == []

    output = capsys.readouterr().out
    assert 'Chrome: ' + I18N['zh']['cookie_diagnostic_permission'] in output
    assert 'Chrome: ' + I18N['zh']['cookie_diagnostic_missing'] not in output
    assert 'private diagnostic text' not in output


@pytest.mark.unit
@pytest.mark.parametrize('error,status', [
    (PermissionError('private diagnostic text'), 'permission'),
    (FileNotFoundError('private diagnostic text'), 'missing'),
    (sqlite3.OperationalError('private diagnostic text'), 'database'),
    (browser_cookie.browser_cookie3.BrowserCookieError(
        'Unable to get key for cookie decryption: private diagnostic text'), 'decryption'),
    (browser_cookie.browser_cookie3.BrowserCookieError(
        'Failed to find cookies for Chrome browser: private diagnostic text'), 'missing'),
    (browser_cookie.browser_cookie3.BrowserCookieError(
        'Could not find Firefox profile directory: private diagnostic text'), 'missing'),
    (browser_cookie.browser_cookie3.BrowserCookieError(
        'Unable to read database file: private diagnostic text'), 'database'),
    (browser_cookie.browser_cookie3.BrowserCookieError('private diagnostic text'), 'error'),
])
def test_probe_classifies_failures_without_exposing_details(error, status, capsys):
    def fail(**kwargs):
        raise error

    diagnostics = []
    assert browser_cookie._probe(fail, 'Chrome', diagnostics) is None
    assert diagnostics == [('Chrome', status)]
    browser_cookie._print_diagnostics(diagnostics)
    assert 'private diagnostic text' not in capsys.readouterr().out


@pytest.mark.unit
def test_diagnostics_distinguishes_empty_store_from_failed_read():
    diagnostics = []
    assert browser_cookie._probe(lambda **kwargs: [], 'Chrome', diagnostics) is None
    assert diagnostics == [('Chrome', 'empty')]


@pytest.mark.unit
def test_diagnostics_reports_missing_dependency_without_reading_browsers(monkeypatch):
    monkeypatch.setattr(browser_cookie, 'HAS_BROWSER_COOKIE', False)
    diagnostics = []
    assert browser_cookie.list_browser_cookies(diagnostics) == []
    assert diagnostics == [('browser-cookie3', 'dependency')]


@pytest.mark.unit
@pytest.mark.parametrize('expired', [False, True])
def test_diagnostic_command_reports_only_status_and_counts(monkeypatch, capsys, expired):
    cookie = _session_cookie({'user_slug': 'private-account',
                              'exp': int(time.time()) + (-3600 if expired else 3600)})

    def fake_candidates(diagnostics):
        diagnostics.extend([('Chrome (Profile 4)', 'found')] * 2)
        return [(cookie, 'Chrome (Profile 4)', 2)]

    monkeypatch.setattr(browser_cookie, 'list_browser_cookies', fake_candidates)

    assert browser_cookie.diagnose_browser_cookies() == int(expired)

    output = capsys.readouterr().out
    assert output.count('Chrome (Profile 4)') == 1
    assert I18N['zh']['cookie_diagnostic_summary'].format(total=1, valid=int(not expired)) in output
    assert cookie not in output
    assert 'LEETCODE_SESSION' not in output
    assert 'private-account' not in output


@pytest.mark.unit
def test_diagnostic_command_exits_before_loading_configuration(monkeypatch):
    from python.scripts import leetcode

    def unexpected_config_access(*args, **kwargs):
        pytest.fail("diagnostics must not load or update configuration")

    monkeypatch.setattr('sys.argv', ['leetcode.py', '--cookie-diagnostics', '--health', '--init'])
    monkeypatch.setattr(leetcode, 'load_dotenv', unexpected_config_access)
    monkeypatch.setattr(leetcode, 'set_key', unexpected_config_access)
    monkeypatch.setattr(leetcode, 'configure', unexpected_config_access)
    monkeypatch.setattr(leetcode, 'initialize_env', unexpected_config_access)
    monkeypatch.setattr(leetcode, 'diagnose_browser_cookies', lambda: 1)

    assert leetcode.main() == 1


# --------------------------------------------------------------------------- #
# Translations for the account picker and browser diagnostics
# --------------------------------------------------------------------------- #

_ACCOUNT_KEYS = {
    'cookie_account_multi': {'options': 'options'},
    'cookie_account_option': {'index': 1, 'user': 'user', 'browser': 'browser',
                              'count': 2, 'state': 'state'},
    'cookie_account_manual': {},
    'cookie_account_pick': {'max': 2},
    'cookie_account_invalid': {'max': 2},
    'cookie_account_expired': {},
    'cookie_account_valid': {},
    'cookie_account_unknown': {},
    'cookie_account_auto': {'user': 'user'},
    'cookie_diagnostic_title': {},
    'cookie_diagnostic_line': {'browser': 'Chrome', 'detail': 'status'},
    **{f'cookie_diagnostic_{status}': {} for status in (
        'found', 'empty', 'missing', 'permission', 'database', 'decryption',
        'error', 'dependency',
    )},
    'cookie_diagnostic_summary': {'total': 1, 'valid': 1},
}


@pytest.mark.unit
@pytest.mark.parametrize('key', sorted(_ACCOUNT_KEYS))
def test_account_picker_strings_defined_in_both_languages(key: str):
    assert key in I18N['zh'], f"missing zh translation: {key}"
    assert key in I18N['en'], f"missing en translation: {key}"


@pytest.mark.unit
@pytest.mark.parametrize('lang', ['zh', 'en'])
def test_account_picker_strings_format_with_caller_arguments(lang: str):
    for key, kwargs in _ACCOUNT_KEYS.items():
        assert I18N[lang][key].format(**kwargs)
