import argparse
import asyncio
import logging
import os
import sys
from pathlib import Path

# Bootstrap: add project root to sys.path before importing python.*
_root = Path(__file__).resolve().parents[2]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from python import lc_libs as lc_libs
from python.constants import constant
from python.utils import (normalize_problem_folder, back_question_id, format_question_id,
                          check_cookie_expired, resolve_link, init_env, adapt_linked_solution_code)

# Process exit statuses. A confirmed "Accepted" result is the only success.
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_CONFIG_ERROR = 2

_LANG_TRANS_MAP = {
    "go": "golang",
    "py": "python3",
    "ts": "typescript",
    "js": "javascript",
    "c++": "cpp",
    "rs": "rust",
}


async def main(root_path: Path, problem_id: str, lang: str, cookie: str,
               problem_folder: str = None, problem_slug: str = None) -> int:
    """Submit a solution and return a process exit status.

    ``EXIT_SUCCESS`` is returned only when LeetCode confirms an Accepted
    result. Missing configuration, unreadable solutions, network failures and
    non-Accepted results return a nonzero status.
    """
    try:
        return await _submit(root_path, problem_id, lang, cookie, problem_folder, problem_slug)
    except Exception as exc:
        logging.error(f"Submission failed: {exc}")
        return EXIT_FAILURE


async def _submit(root_path: Path, problem_id: str, lang: str, cookie: str,
                  problem_folder: str = None, problem_slug: str = None) -> int:
    # Normalize the folder before any path is built so an unset PROBLEM_FOLDER
    # falls back to the documented default instead of propagating None.
    folder_configured = bool((problem_folder or "").strip())
    problem_folder = normalize_problem_folder(problem_folder)

    if not cookie:
        logging.error("Cookie is required to submit; configure COOKIE in the environment or .env.")
        return EXIT_CONFIG_ERROR
    if check_cookie_expired(cookie):
        logging.warning("LeetCode cookie might have expired; please check!")

    lang = _LANG_TRANS_MAP.get(lang.lower(), lang)
    load_code = False
    code = ""
    cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
    if not cls:
        logging.error(f"{lang} writer is not supported yet!")
        return EXIT_CONFIG_ERROR
    obj: lc_libs.LanguageWriter = cls()
    if not problem_id:
        code, problem_id = obj.get_solution_code(root_path, problem_folder, problem_id)
        if not code:
            logging.error("No solution yet!")
            return EXIT_FAILURE
        if not problem_id:
            logging.error(f"Unable to get problem_id: {problem_id}, check input or environment folder")
            return EXIT_CONFIG_ERROR
        load_code = True
        # Check if this is the daily problem (only when not explicitly specified via -id/-slug)
        try:
            daily_info = lc_libs.get_daily_question()
            if daily_info:
                daily_id = daily_info.get("questionId", "")
                if daily_id and format_question_id(daily_id) != problem_id:
                    logging.warning(
                        f"⚠️  当前提交的题目 [{problem_id}] 不是今日每日一题 [{daily_id}]！"
                        f"请确认是否在正确的分支上提交。"
                    )
        except Exception as e:
            logging.warning(f"无法检查每日一题状态: {e}")

    # Resolve link if exists (only for code, not for problem ID)
    link_info = None
    solution_problem_id = problem_id
    solution_folder = problem_folder
    problem_path = root_path / problem_folder / f"{problem_folder}_{problem_id}"
    if problem_path.exists():
        solution_path, link_info = resolve_link(problem_path)
        if link_info:
            linked_problem_id = link_info["link_to"]
            linked_folder = link_info.get("link_folder", problem_folder)
            logging.info(f"Problem {problem_id} uses solution from {linked_problem_id}: {link_info.get('reason', 'No reason provided')}")
            solution_problem_id = linked_problem_id
            solution_folder = linked_folder

    if not problem_slug:
        origin_problem_id = back_question_id(problem_id)
        questions = lc_libs.get_questions_by_key_word(origin_problem_id, cookie)
        if not questions:
            logging.error(f"Unable to find any questions with LeetCode problem_id {origin_problem_id},"
                          f"check the input problem_id or contact the author")
            return EXIT_FAILURE
        for question in questions:
            if question["questionFrontendId"] == origin_problem_id:
                problem_slug = question["titleSlug"]
                break
        if not problem_slug:
            logging.warning(
                f"Unable to find any questions with problem_id {origin_problem_id}, possible questions:\n"
                + "\n".join(v["questionFrontendId"] for v in questions))
            return EXIT_CONFIG_ERROR
    problem_info = lc_libs.get_question_info(problem_slug, cookie)
    if not problem_info:
        logging.warning(f"Unable to get problem info, possibly network issue, slug: {problem_slug}")
        return EXIT_FAILURE
    is_paid_only = problem_info["isPaidOnly"]
    if not folder_configured:
        # Paid-only problems live in the "premiums" folder unless the user
        # configured an explicit folder.
        problem_folder = normalize_problem_folder(None, paid_only=is_paid_only)
        if not link_info:
            solution_folder = problem_folder
    if not load_code:
        code, _ = obj.get_solution_code(root_path, solution_folder, solution_problem_id)
        if not code:
            logging.error(f"No solution for problem [{problem_id}.{problem_slug}] yet!")
            return EXIT_FAILURE
        # If this problem is linked to another with a different method name
        # (e.g. 1081 smallestSubsequence vs 316 removeDuplicateLetters), LeetCode
        # expects the current problem's method name. Rewrite the linked solution.
        if link_info and problem_id != solution_problem_id:
            code = adapt_linked_solution_code(
                root_path, problem_folder, problem_id,
                solution_folder, solution_problem_id, lang, code, obj.solution_file
            )
    lc_question_id = problem_info["questionId"]
    plans = lc_libs.get_user_study_plans(cookie)
    if plans is None:
        logging.error("Cookie might be expired, please check the cookie")
        return EXIT_CONFIG_ERROR
    result = None
    exists = False
    for i, plan in enumerate(plans):
        all_problems = lc_libs.get_user_study_plan_progress(plan, cookie, 0).get("all_problems", set())
        if problem_slug in all_problems:
            if i > 0:
                await asyncio.sleep(1)
            logging.info("Submit code in plan [{}] problem: {}".format(plan, problem_slug))
            result = await lc_libs.submit_code(root_path, problem_folder, problem_id, problem_slug, cookie, lang,
                                               lc_question_id, code, plan)
            if result:
                exists = True
                if result.get("statusDisplay") != "Accepted":
                    break
    if not exists:
        result = await lc_libs.submit_code(root_path, problem_folder, problem_id, problem_slug, cookie, lang,
                                           lc_question_id, code)
    if not result:
        logging.error("No submission result was returned; check network connectivity and login state")
        return EXIT_FAILURE
    status = result.get("statusDisplay")
    if status != "Accepted":
        logging.error(f"Submission finished with status [{status or 'Unknown'}], not Accepted")
        exit_code = EXIT_FAILURE
    else:
        exit_code = EXIT_SUCCESS
    # Display popular solutions. Article retrieval is optional and must not
    # invalidate a confirmed Accepted submission.
    try:
        articles_result = lc_libs.get_answer_articles(problem_slug, cookie, first=5) or {}
        articles = articles_result.get("articles", [])
        if articles:
            logging.info("热门题解:")
            for i, article in enumerate(articles, 1):
                author_info = article.get("author", {})
                profile = author_info.get("profile", {})
                author_name = profile.get("realName", "") or author_info.get("username", "Unknown")
                title = article.get("title", "")[:40]
                upvote = article.get("upvoteCount", 0)
                topic_id = article.get("topic", {}).get("id", "")
                article_slug = article.get("slug", "")
                solution_link = f"https://leetcode.cn/problems/{problem_slug}/solutions/{topic_id}/{article_slug}/" if topic_id and article_slug else ""
                logging.info(f"  {i}. {title}{'...' if len(article.get('title', '')) > 40 else ''} | {author_name} | 👍{upvote}")
                if solution_link:
                    logging.info(f"     🔗 {solution_link}")
        else:
            logging.info("未找到社区题解")
    except Exception as e:
        logging.warning(f"获取题解失败: {e}")
    return exit_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Submit a local solution to LeetCode.")
    parser.add_argument("-id", required=False, type=str, help="The id of question to submit.", default="")
    parser.add_argument("-slug", required=False, type=str,
                        help="The slug of question to submit. "
                             "Usually useful when problem id not update to the latest in leetcode.", default="")
    parser.add_argument("lang", choices=list(_LANG_TRANS_MAP.keys()) +
                                        ["java"] + list(_LANG_TRANS_MAP.values()))
    parser.add_argument("-d", "--daily", required=False, action="store_true",
                        help="To daily submission.")
    return parser


def run(argv=None) -> int:
    """Parse CLI arguments, load configuration and submit.

    ``--help`` exits successfully through argparse before any environment or
    network work happens.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    init_env()
    if args.daily:
        try:
            daily_question = lc_libs.get_daily_question()
        except Exception as exc:
            logging.error(f"Unable to get the daily question: {exc}")
            return EXIT_FAILURE
        if not daily_question or not daily_question.get("questionId"):
            logging.error("Unable to get the daily question; check network connectivity")
            return EXIT_FAILURE
        question_id = daily_question["questionId"]
    else:
        question_id = args.id
    slug = args.slug
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER)
    log_level = os.getenv(constant.LOG_LEVEL, "INFO")
    level = logging.getLevelName(log_level.upper())
    logging.basicConfig(level=level if isinstance(level, int) else logging.INFO,
                        format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    rp = Path(__file__).parent.parent.parent
    return asyncio.run(main(rp, format_question_id(question_id),
                            args.lang, cke, pf, problem_slug=slug))


if __name__ == '__main__':
    sys.exit(run())
