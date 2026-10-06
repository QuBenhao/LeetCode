import itertools
import logging
import urllib.parse
from typing import Optional, List, Dict

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


def get_answer_endlesscheng(problem_slug: str, cookie: str) -> Optional[Dict]:
    """
    Get the solution by endlesscheng (灵茶山艾府) for the specified problem

    Args:
        problem_slug: Problem slug
        cookie: LeetCode Cookie

    Returns:
        Dictionary of solution content (including title, content, author, etc.); None if not found
    """
    if not cookie:
        logging.warning("Cookie is empty, cannot fetch endlesscheng solution")
        return None
    from python.lc_libs.solution_article import get_solution_by_author
    return get_solution_by_author(problem_slug, "endlesscheng", cookie)


def get_answer_articles(problem_slug: str, cookie: str, first: int = 5, skip: int = 0) -> Dict:
    """
    Get popular community solutions for the specified problem

    Args:
        problem_slug: Problem slug
        cookie: LeetCode Cookie
        first: Number of results to return; defaults to 5
        skip: Number of results to skip; defaults to 0 (for pagination)

    Returns:
        Dictionary containing:
        - total: Total count
        - articles: List of solutions, each containing slug, title, author, upvoteCount, hitCount, summary, etc.
    """
    if not cookie:
        logging.warning("Cookie is empty, cannot fetch solution articles")
        return {"total": 0, "articles": []}
    from python.lc_libs.solution_article import get_solution_articles
    return get_solution_articles(problem_slug, cookie, first=first, skip=skip)
