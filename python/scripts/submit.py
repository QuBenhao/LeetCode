import argparse
import asyncio
import logging
import os
import sys
import traceback
from pathlib import Path

from dotenv import load_dotenv

sys.path.append(Path(__file__).parent.parent.parent.as_posix())
from python import lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, back_question_id, format_question_id, check_cookie_expired

_LANG_TRANS_MAP = {
    "go": "golang",
    "py": "python3",
    "ts": "typescript",
    "js": "javascript",
    "c++": "cpp",
    "rs": "rust",
}


async def main(root_path: Path, problem_id: str, lang: str, cookie: str,
               problem_folder: str = None, check_solution: bool = False):
    if check_cookie_expired(cookie):
        logging.warning("LeetCode cookie might have expired; please check!")
    lang = _LANG_TRANS_MAP.get(lang.lower(), lang)
    load_code = False
    code = ""
    cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
    if not cls:
        logging.warning(f"{lang} writer is not supported yet!")
        return
    obj: lc_libs.LanguageWriter = cls()
    if not problem_id:
        if not problem_folder:
            problem_folder = get_default_folder()
        code, problem_id = obj.get_solution_code(root_path, problem_folder, problem_id)
        if not code:
            logging.error("No solution yet!")
            return
        if not problem_id:
            logging.error(f"Unable to get problem_id: {problem_id}, check input or environments folder")
            return
        load_code = True
    origin_problem_id = back_question_id(problem_id)
    questions = lc_libs.get_questions_by_key_word(origin_problem_id)
    if not questions:
        logging.error(f"Unable to find any questions with LeetCode problem_id {origin_problem_id},"
                      f"check the input problem_id or contact the author")
        return
    problem_slug = None
    for question in questions:
        if question["paidOnly"] and not cookie:
            continue
        if question["frontendQuestionId"] == origin_problem_id:
            problem_slug = question["titleSlug"]
            break
    if not problem_slug:
        logging.warning(
            f"Unable to find any questions with problem_id {origin_problem_id}, possible questions:\n"
            + "\n".join(v for v in questions))
        return
    problem_info = lc_libs.get_question_info(problem_slug, cookie)
    if not problem_info:
        logging.warning(f"Unable to get problem info, possibly network issue, slug: {problem_slug}")
        return
    is_paid_only = problem_info["isPaidOnly"]
    if not problem_folder:
        problem_folder = get_default_folder(paid_only=is_paid_only)
    if not load_code:
        code, _ = obj.get_solution_code(root_path, problem_folder, problem_id)
        if not code:
            logging.error(f"No solution for problem [{problem_id}.{problem_slug}] yet!")
            return
    lc_question_id = problem_info["questionId"]
    plans = lc_libs.get_user_study_plans(cookie)
    if plans is None:
        logging.error("Cookie might be expired, please check the cookie")
        return
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
            exists = True
            if result and result["statusDisplay"] != "Accepted":
                break
    if not exists:
        result = await lc_libs.submit_code(root_path, problem_folder, problem_id, problem_slug, cookie, lang,
                                           lc_question_id, code)
    logging.info(f"题解查看: https://leetcode.cn/problems/{problem_slug}/solutions/")
    logging.info(f"外网查看: https://leetcode.com/problems/{problem_slug}/solutions/")
    if check_solution:
        san_ye_solution = lc_libs.get_answer_san_ye(problem_id, problem_slug)
        if san_ye_solution:
            logging.info(f"参考题解: {san_ye_solution}")
        else:
            logging.warning(f"未找到参考题解")
    return result


if __name__ == '__main__':
    rp = Path(__file__).parent.parent.parent
    sys.path.insert(0,str(rp / "python"))
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", required=False, type=str, help="The id of question to submit.", default="")
    parser.add_argument("-solution", required=False, action="store_true", help="Check SanYe solution.")
    parser.add_argument("lang", choices=list(_LANG_TRANS_MAP.keys()) +
                                        ["java"] + list(_LANG_TRANS_MAP.values()))
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    question_id = args.id
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, None)
    log_level = os.getenv(constant.LOG_LEVEL, "INFO")
    logging.basicConfig(level=log_level.upper(), format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    try:
        langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    except Exception as _:
        logging.warning("Load languages failed, use default python3", exc_info=True)
        langs = ["python3"]
    if sys.version_info.major == 3 and sys.version_info.minor > 10:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(main(rp, format_question_id(question_id), args.lang, cke, pf, args.solution))
    sys.exit(0)
