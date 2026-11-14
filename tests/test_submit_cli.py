"""Regression tests for the Python submission CLI (``python/scripts/submit.py``).

LeetCode responses are mocked and problems live in isolated temporary
directories, so these tests never contact the network or read credentials.
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path

import pytest

from python.constants import constant
from python.scripts import submit
from python.utils import normalize_problem_folder

pytestmark = pytest.mark.unit

PROBLEM_ID = "1524"
PROBLEM_SLUG = "number-of-sub-arrays-with-odd-sum"
COOKIE = "LEETCODE_SESSION=test-session"
ACCEPTED = {"statusDisplay": "Accepted", "passedTestCaseCnt": 1, "totalTestCaseCnt": 1}
WRONG_ANSWER = {"statusDisplay": "Wrong Answer", "passedTestCaseCnt": 0, "totalTestCaseCnt": 1}


class FakeWriter:
    """Minimal LanguageWriter replacement that records folder lookups."""

    solution_file = "solution.py"

    def __init__(self, code="class Solution:\n    pass\n"):
        self.code = code
        self.calls = []

    def get_solution_code(self, root_path: Path, problem_folder: str, problem_id: str):
        self.calls.append((problem_folder, problem_id))
        return self.code, problem_id or PROBLEM_ID


class Harness:
    def __init__(self):
        self.writer = FakeWriter()
        self.state = {
            "result": ACCEPTED,
            "is_paid_only": False,
            "questions_error": None,
            "articles_error": None,
        }
        self.submit_calls = []

    async def submit_code(self, root_path, problem_folder, question_id, question_slug, cookie, lang,
                          leetcode_question_id, code, study_plan_slug=None):
        self.submit_calls.append({
            "folder": problem_folder,
            "question_id": question_id,
            "slug": question_slug,
            "lang": lang,
            "code": code,
            "plan": study_plan_slug,
        })
        return self.state["result"]

    def questions(self, problem_id, cookie):
        if self.state["questions_error"]:
            raise self.state["questions_error"]
        return [{"questionFrontendId": problem_id, "titleSlug": PROBLEM_SLUG}]

    def question_info(self, slug, cookie):
        return {"isPaidOnly": self.state["is_paid_only"], "questionId": "1600"}

    def articles(self, slug, cookie, first=5):
        if self.state["articles_error"]:
            raise self.state["articles_error"]
        return {"articles": []}


@pytest.fixture
def harness(monkeypatch):
    h = Harness()
    monkeypatch.setattr(submit, "check_cookie_expired", lambda cookie: False)
    monkeypatch.setattr(submit.lc_libs, "Python3Writer", lambda: h.writer)
    monkeypatch.setattr(submit.lc_libs, "get_questions_by_key_word", h.questions)
    monkeypatch.setattr(submit.lc_libs, "get_question_info", h.question_info)
    monkeypatch.setattr(submit.lc_libs, "get_user_study_plans", lambda cookie: [])
    monkeypatch.setattr(submit.lc_libs, "get_user_study_plan_progress",
                        lambda plan, cookie, offset: {"all_problems": set()})
    monkeypatch.setattr(submit.lc_libs, "get_daily_question", lambda: {"questionId": PROBLEM_ID})
    monkeypatch.setattr(submit.lc_libs, "submit_code", h.submit_code)
    monkeypatch.setattr(submit.lc_libs, "get_answer_articles", h.articles)
    return h


@pytest.fixture
def cli(monkeypatch, harness):
    monkeypatch.setattr(submit, "init_env", lambda: None)
    monkeypatch.setenv(constant.COOKIE, COOKIE)
    monkeypatch.delenv(constant.PROBLEM_FOLDER, raising=False)
    return harness


def _make_problem(root: Path, folder: str, problem_id: str = PROBLEM_ID, text="class Solution:\n    pass\n"):
    problem_dir = root / folder / f"{folder}_{problem_id}"
    problem_dir.mkdir(parents=True)
    (problem_dir / "solution.py").write_text(text, encoding="utf-8")
    return root


def test_normalize_problem_folder_defaults_and_overrides():
    assert normalize_problem_folder(None) == "problems"
    assert normalize_problem_folder("") == "problems"
    assert normalize_problem_folder("  ") == "problems"
    assert normalize_problem_folder("mysql") == "mysql"
    assert normalize_problem_folder("premiums") == "premiums"
    assert normalize_problem_folder(None, paid_only=True) == "premiums"
    assert normalize_problem_folder("mysql", paid_only=True) == "mysql"
    assert normalize_problem_folder(None, problem_category="database") == "mysql"


def test_explicit_id_with_unset_folder_uses_default(tmp_path, harness):
    """The historical crash built ``root/None`` before defaulting the folder."""
    _make_problem(tmp_path, "problems")

    status = asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE, None))

    assert status == submit.EXIT_SUCCESS
    assert harness.writer.calls[0][0] == "problems"
    assert harness.submit_calls[0]["folder"] == "problems"


def test_explicit_folder_override_is_preserved(tmp_path, harness):
    _make_problem(tmp_path, "mysql", "175", text="SELECT 1;\n")

    status = asyncio.run(submit.main(tmp_path, "175", "python3", COOKIE, " mysql "))

    assert status == submit.EXIT_SUCCESS
    assert harness.writer.calls[0][0] == "mysql"
    assert harness.submit_calls[0]["folder"] == "mysql"


def test_paid_only_problem_uses_premiums_when_folder_unset(tmp_path, harness):
    harness.state["is_paid_only"] = True
    _make_problem(tmp_path, "premiums", "156")

    status = asyncio.run(submit.main(tmp_path, "156", "python3", COOKIE, None))

    assert status == submit.EXIT_SUCCESS
    assert harness.submit_calls[0]["folder"] == "premiums"


def test_slug_invocation_with_unset_folder(tmp_path, harness):
    _make_problem(tmp_path, "problems")

    status = asyncio.run(submit.main(tmp_path, "", "python3", COOKIE, None, problem_slug=PROBLEM_SLUG))

    assert status == submit.EXIT_SUCCESS
    assert harness.submit_calls[0]["slug"] == PROBLEM_SLUG
    assert harness.submit_calls[0]["folder"] == "problems"


def test_daily_mode_through_cli_uses_default_folder(cli):
    status = submit.run(["-d", "python3"])

    assert status == submit.EXIT_SUCCESS
    assert cli.submit_calls[0]["folder"] == "problems"
    assert cli.submit_calls[0]["question_id"] == PROBLEM_ID


def test_cli_explicit_id_flow_uses_env_cookie(cli):
    status = submit.run(["-id", PROBLEM_ID, "python3"])

    assert status == submit.EXIT_SUCCESS
    assert cli.submit_calls[0]["folder"] == "problems"
    assert cli.submit_calls[0]["lang"] == "python3"


def test_accepted_is_success(harness, tmp_path):
    _make_problem(tmp_path, "problems")

    assert asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE)) == 0


def test_non_accepted_is_failure(harness, tmp_path):
    harness.state["result"] = WRONG_ANSWER
    _make_problem(tmp_path, "problems")

    status = asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE))

    assert status == submit.EXIT_FAILURE
    assert status != submit.EXIT_SUCCESS


def test_missing_result_is_failure(harness, tmp_path):
    harness.state["result"] = None
    _make_problem(tmp_path, "problems")

    assert asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE)) == submit.EXIT_FAILURE


def test_missing_solution_is_failure(harness, tmp_path):
    harness.writer.code = ""

    assert asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE)) == submit.EXIT_FAILURE


def test_missing_credentials_is_config_error(cli, monkeypatch):
    monkeypatch.setenv(constant.COOKIE, "")

    status = submit.run(["-id", PROBLEM_ID, "python3"])

    assert status == submit.EXIT_CONFIG_ERROR
    assert cli.submit_calls == []


def test_network_exception_is_failure(harness, tmp_path):
    harness.state["questions_error"] = ConnectionError("network down")
    _make_problem(tmp_path, "problems")

    status = asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE))

    assert status == submit.EXIT_FAILURE


def test_article_retrieval_failure_keeps_accepted_success(harness, tmp_path):
    harness.state["articles_error"] = RuntimeError("articles unavailable")
    _make_problem(tmp_path, "problems")

    assert asyncio.run(submit.main(tmp_path, PROBLEM_ID, "python3", COOKIE)) == submit.EXIT_SUCCESS


def test_help_is_offline_success(monkeypatch):
    def fail_if_called():
        raise AssertionError("init_env must not run for --help")

    monkeypatch.setattr(submit, "init_env", fail_if_called)

    with pytest.raises(SystemExit) as exc_info:
        submit.run(["--help"])

    assert exc_info.value.code == 0


def test_script_entry_point_reaches_credential_check():
    """Exercise real argparse/env flow without network or a real cookie.

    An explicitly empty COOKIE wins over any local .env value, so the script
    stops at the credential check with the configuration exit status.
    """
    env = os.environ.copy()
    env[constant.COOKIE] = ""
    env.pop(constant.PROBLEM_FOLDER, None)
    script = Path(__file__).resolve().parents[1] / "python" / "scripts" / "submit.py"

    completed = subprocess.run(
        [sys.executable, str(script), "-id", PROBLEM_ID, "python3"],
        cwd=Path(__file__).resolve().parents[1],
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert completed.returncode == submit.EXIT_CONFIG_ERROR, completed.stderr
    assert "Cookie is required" in completed.stderr
