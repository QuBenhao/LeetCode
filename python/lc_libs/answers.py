import itertools
import logging
import urllib.parse
from typing import Optional, List

from python.utils.http_tool import github_iterate_repo, github_get_file_content
from python.utils.str_util import back_question_id

BASE_URL = "https://github.com/SharingSource/LogicStack-LeetCode/blob/main/"
SAN_YE = "SharingSource"
REPO = "LogicStack-LeetCode"
BRANCH = "main"


def _get_file_solution_line(file_path) -> Optional[str]:
    content = github_get_file_content(SAN_YE, REPO, file_path, BRANCH)
    if not content:
        return None
    for line in content.split("\n"):
        if "https://leetcode.cn/problems/" in line \
                or "https://leetcode-cn.com/problems/" in line \
                or "https://leetcode.com/problems/" in line:
            return line
    logging.debug(f"Solution line not found in file: {file_path}, content: {content}")
    return None


def _find_by_slug(problem_id: str, problem_slug: Optional[str], possible_files: List[str]) -> Optional[str]:
    for file_path in possible_files:
        sol_line = _get_file_solution_line(file_path)
        if not sol_line:
            continue
        if problem_slug and problem_slug in sol_line:
            return file_path
        if problem_id in sol_line:
            return file_path
    return None


def get_answer_san_ye(problem_id: str, problem_slug: Optional[str] = None) -> Optional[str]:
    origin_id = back_question_id(problem_id)
    source = github_iterate_repo(SAN_YE, REPO, BRANCH, "LeetCode")
    if not source:
        return None
    if origin_id.isnumeric():
        num = int(origin_id)
        rg = (num - 1) // 10 * 10
        folder = f"{rg + 1}-{rg + 10}"
        for file in source:
            if file.startswith(f"LeetCode/{folder}/{origin_id}."):
                return BASE_URL + urllib.parse.quote(file)
        logging.debug("Solution not found for problem id: " + problem_id)
    if origin_id.startswith("LCR "):
        possibles = list(itertools.filterfalse(lambda x: "LCR" not in x and "剑指 Offer" not in x, source))
        logging.debug(possibles)
        file = _find_by_slug(origin_id + ".", problem_slug, possibles)
        if file:
            return BASE_URL + urllib.parse.quote(file)
        logging.debug(f"Solution not found for problem id: {problem_id} and problem slug: {problem_slug}")
    return None
