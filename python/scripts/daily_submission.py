import logging
import os
import sys
import traceback
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from daily_auto import write_question

sys.path.append(Path(__file__).parent.parent.parent.as_posix())
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message, check_cookie_expired


def main(cookie: Optional[str], languages: list[str], problem_folder: str = None, user_slug: str = None):
    try:
        if check_cookie_expired(cookie):
            logging.warning("LeetCode cookie may have expired; please check!")
        daily_info = lc_libs.get_daily_question()
        if not daily_info:
            logging.error(f"Unable to get daily question, possibly network issue?")
            return 1
        daily_question = daily_info['questionId']
        finish_daily = False
        plan_questions_slug = set()
        finished_plan_questions = []
        if cookie:
            plans = lc_libs.get_user_study_plans(cookie)
            if plans is None:
                if not send_text_message("The LeetCode in GitHub secrets might be expired, please check!",
                                         "Currently might not be able to fetch submission."):
                    logging.error("Unable to send PushDeer notification!")
                logging.warning("The LeetCode cookie might be expired!")
            elif plans:
                for plan_slug in plans:
                    plan_prog = lc_libs.get_user_study_plan_progress(plan_slug, cookie, 0)
                    plan_questions_slug = plan_questions_slug.union(plan_prog["all_solved"])
        if cookie:
            submit_dict = lc_libs.check_accepted_submission_all(cookie)
        else:
            if not user_slug or not lc_libs.check_user_exist(user_slug):
                logging.error(f"User not exist: {user_slug}")
                return 1
            submit_dict = lc_libs.check_accepted_submission(user_slug)
        root_path = Path(__file__).parent.parent.parent
        sys.path.insert(0, str(root_path / "python"))
        for question_id, submits in submit_dict.items():
            cache = set()
            info = None
            if problem_folder:
                tmp_problem_folder = problem_folder
            elif question_id == daily_question:
                tmp_problem_folder = get_default_folder()
            else:
                info = lc_libs.get_question_info(submits[0][1], cookie)
                tmp_problem_folder = get_default_folder(paid_only=info.get("isPaidOnly", False))
            dir_path = root_path / tmp_problem_folder / f"{tmp_problem_folder}_{question_id}"
            if question_id == daily_question and not dir_path.exists():
                dir_path.mkdir(parents=True, exist_ok=True)
                write_question(root_path, dir_path, tmp_problem_folder, daily_question, daily_info['questionNameEn'],
                               daily_info['questionSlug'], list(languages), cookie)
            elif dir_path.exists():
                if not info:
                    info = lc_libs.get_question_info(submits[0][1], cookie)
                dir_path.mkdir(parents=True, exist_ok=True)
                write_question(root_path, dir_path, tmp_problem_folder, question_id, info["title"],
                               submits[0][1], list(languages), cookie)
            default_code = lc_libs.get_question_code(submits[0][1], lang_slugs=languages, cookie=cookie)
            for submit_id, question_slug, language in submits:
                if language in cache:
                    continue
                detail = lc_libs.get_submission_detail(submit_id, cookie)
                if detail["statusDisplay"] != "Accepted":
                    logging.debug(f"Wrong solution for question {question_slug}, {detail['statusDisplay']}")
                    continue
                if not detail:
                    logging.warning(f"Unable to get submission detail for {submit_id}")
                    continue
                if detail["lang"] not in default_code:
                    logging.warning(f"Language {detail['lang']} is not added to check submission,"
                                    f" please add it if needed")
                    continue
                code = detail["code"]
                cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
                if not cls:
                    logging.warning("Language Writer not supported yet")
                    continue
                obj: lc_libs.LanguageWriter = cls()
                if obj.run_code(root_path, tmp_problem_folder, question_id,
                                True, default_code[detail["lang"]], code):
                    logging.warning(f"Already solved problem: {question_id}, language: {language}")
                else:
                    logging.info(f"Add [{language}] solution for problem: {question_id}")
                cache.add(language)
                if question_id == daily_question:
                    finish_daily = True
                elif question_slug in plan_questions_slug and question_slug not in finished_plan_questions:
                    finished_plan_questions.append(question_slug)
        logging.info("Daily Question {}: {}, Study plan problem solved today: {}"
                     .format(daily_question, "DONE" if finish_daily else "TODO", finished_plan_questions))
        if not finish_daily:
            return 1
    except Exception as _:
        logging.error("Daily submission error", exc_info=True)
        return 1
    return 0


if __name__ == '__main__':
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, None)
    ur = os.getenv(constant.USER, None)
    log_level = os.getenv(constant.LOG_LEVEL, "INFO")
    logging.basicConfig(level=log_level.upper(), format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    try:
        langs_str = os.getenv(constant.LANGUAGES, "python3")
        if not langs_str:
            langs_str = "python3"
        langs = langs_str.split(",")
    except Exception as _:
        logging.warning("Load languages failed, use default python3", exc_info=True)
        langs = ["python3"]
    exec_res = main(cke, langs, pf, ur)
    sys.exit(exec_res)
