"""Tests for testcase deduplication in ``python.lc_libs.submission._add_test``."""

import pytest

from python.lc_libs.submission import _add_test

PROBLEM_FOLDER = "problems"
QUESTION_ID = "3963"

TESTCASE_PY = """from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
\tdef __init__(self):
\t\tself.testcases = []
\t\tself.testcases.append(case(Input=[2, 3], Output=['..#', '#..']))

\tdef get_testcases(self):
\t\treturn self.testcases
"""


def _make_problem(tmp_path, testcase_file=None):
    """Create a minimal problem folder and return the root path passed to _add_test."""
    dir_path = tmp_path / PROBLEM_FOLDER / f"{PROBLEM_FOLDER}_{QUESTION_ID}"
    dir_path.mkdir(parents=True)
    (dir_path / "testcase.py").write_text(TESTCASE_PY, encoding="utf-8")
    if testcase_file is not None:
        (dir_path / "testcase").write_text(testcase_file, encoding="utf-8")
    return tmp_path


def _read(tmp_path, name):
    return (tmp_path / PROBLEM_FOLDER / f"{PROBLEM_FOLDER}_{QUESTION_ID}" / name).read_text(encoding="utf-8")


@pytest.mark.unit
def test_add_test_skips_example_case_with_json_quoting(tmp_path):
    """Example cases use Python repr quoting; submission details use JSON quoting."""
    root = _make_problem(tmp_path)

    _add_test(root, PROBLEM_FOLDER, QUESTION_ID, "[2,3]", '["..#","#.."]')

    assert _read(tmp_path, "testcase.py") == TESTCASE_PY


@pytest.mark.unit
def test_add_test_appends_new_case(tmp_path):
    root = _make_problem(tmp_path)

    _add_test(root, PROBLEM_FOLDER, QUESTION_ID, "[5,5]", '[".....","....."]')

    content = _read(tmp_path, "testcase.py")
    assert content.count("Input=[5,5]") == 1


@pytest.mark.unit
def test_testcase_file_skips_identical_pair(tmp_path):
    testcase_file = '["2\\n3"]\n[["..#", "#.."]]'
    root = _make_problem(tmp_path, testcase_file)

    _add_test(root, PROBLEM_FOLDER, QUESTION_ID, "2\n3", '["..#", "#.."]')

    assert _read(tmp_path, "testcase") == testcase_file


@pytest.mark.unit
def test_testcase_file_adds_pair_whose_output_is_a_sublist(tmp_path):
    """An output that merely occurs inside another case is not a duplicate."""
    testcase_file = '["2\\n3"]\n[["..#", "#.."]]'
    root = _make_problem(tmp_path, testcase_file)

    _add_test(root, PROBLEM_FOLDER, QUESTION_ID, "2\n3", '["..#"]')

    content = _read(tmp_path, "testcase")
    assert '["2\\n3", "2\\n3"]' in content
    assert '[["..#", "#.."], ["..#"]]' in content
