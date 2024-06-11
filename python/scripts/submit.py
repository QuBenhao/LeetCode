import asyncio
import os
import sys
import traceback
import argparse
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message


async def main(root_path, problem_id: str, lang: str, cookie: str, problem_folder: str = None):
    if not problem_folder:
        problem_folder = get_default_folder()
    code_func = getattr(lc_libs, "get_solution_code_{}".format(lang), None)
    if not code_func:
        print(f"{lang} is not supported yet!")
        return
    code, problem_id = code_func(root_path, problem_folder, problem_id)
    if not code:
        print("No solution yet!")
        return
    if not problem_id:
        print("Unable to get problem_id")
        return
    questions = lc_libs.get_questions_by_key_word(problem_id)
    if not questions:
        print(f"Unable to find any questions with problem_id {problem_id}")
        return
    problem_slug = None
    for question in questions:
        if question["paidOnly"] and not cookie:
            continue
        if question["frontendQuestionId"] == problem_id:
            problem_slug = question["titleSlug"]
            break
    if not problem_slug:
        print(f"Unable to find any questions with problem_id {problem_id}, possible questions: {questions}")
        return
    problem_info = lc_libs.get_question_info(problem_slug, cookie)
    if not problem_info:
        print(f"Unable to get problem info: {problem_id}")
        return
    lc_question_id = problem_info["questionId"]
    result = await lc_libs.submit_code(problem_slug, cookie, lang, lc_question_id, code)
    return result


if __name__ == '__main__':
    rp = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(rp, "python"))
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", required=False, type=str, help="The id of question to submit.", default="")
    parser.add_argument("lang", type=str, help="The language to submit.")
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    question_id = args.id
    cke = os.getenv(constant.COOKIE)
    try:
        langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    except Exception as _:
        traceback.print_exc()
        langs = ["python3"]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(rp, question_id, args.lang, cke))
    sys.exit(0)
