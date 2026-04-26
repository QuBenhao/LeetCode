#!/usr/bin/env python3
"""
LeetCode 工具集 - 主入口
支持交互式初始化、浏览器 Cookie 自动检测、多语言界面

使用方法：
  python leetcode.py           # 默认中文界面
  python leetcode.py --en      # 英文界面
  python leetcode.py --init    # 强制进入初始化向导
"""

import argparse
import asyncio
import datetime
import json
import logging
import math
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv, set_key

# Setup paths
file_path = Path(__file__)
root_path = file_path.parent.parent.parent
sys.path.insert(0, root_path.as_posix())

# Import CLI modules
from python.scripts.cli import (
    t, set_language, get_language,
    input_until_valid, input_pick_array,
    get_browser_cookie, read_cookie_from_file, HAS_BROWSER_COOKIE,
    check_and_update_cookie,
)
from python.scripts.cli.input_utils import allow_all, allow_all_not_empty, allow_number

# Import LeetCode libraries
from python.constants import constant
from python.lc_libs import get_daily_question, query_my_favorites, batch_add_questions_to_favorite, \
    query_favorite_questions, contest as contest_lib
import python.lc_libs as lc_libs
from python.scripts.submit import main as submit_main_async
from python.utils import back_question_id, format_question_id, check_cookie_expired, create_link
from python.scripts.daily_auto import main as daily_auto_main
from python.scripts.get_problem import main as get_problem_main, get_question_slug_by_id
from python.scripts.tools import lucky_main, remain_main, clean_empty_java_main, clean_error_rust_main
from python.scripts.fetch_solution_articles import main as fetch_solution_main

# Constants
SEPARATE_LINE = "-" * 50
SUPPORTED_LANGUAGES = ["python3", "java", "golang", "cpp", "typescript", "rust"]


# ============================================================================
# Initialization and Configuration
# ============================================================================

def initialize_env():
    """Interactive environment initialization wizard"""
    print("\n" + "=" * 50)
    print(t("init_title"))
    print("=" * 50)

    env_file = root_path / ".env"

    # Step 1: Auto-detect browser cookie
    print(f"\n{t('init_step1')}")
    cookie = None
    max_retries = 3
    retry_count = 0
    if HAS_BROWSER_COOKIE:
        while retry_count < max_retries:
            result = get_browser_cookie()
            if result:
                cookie, browser_name, cookie_count = result
                print(t("init_found_cookie", browser=browser_name, count=cookie_count))
                # Verify cookie immediately
                print(t("init_verifying"))
                if check_cookie_expired(cookie):
                    print(t("init_cookie_invalid"))
                    print(t("cookie_auto_expired_hint"))
                    retry = input_until_valid(t("init_retry_login"), allow_all)
                    if retry != "n":
                        retry_count += 1
                        if retry_count >= max_retries:
                            print(t("init_max_retries"))
                            cookie = None
                            break
                        print(t("init_waiting_login"))
                        input()  # Wait for user to press Enter after logging in
                        continue
                    else:
                        cookie = None
                else:
                    print(t("init_cookie_valid"))
                break
            else:
                print(t("init_no_cookie"))
                print(t("cookie_no_browser_hint"))
                break
    else:
        print(t("init_browser_not_installed"))
        print(t("init_browser_install_hint"))

    if not cookie:
        cookie = read_cookie_from_file()
        if not cookie:
            cookie = input_until_valid(
                t("init_enter_cookie"),
                allow_all_not_empty,
                t("init_cookie_empty")
            )
    print(SEPARATE_LINE)

    # Load existing config or use defaults
    if env_file.exists():
        try:
            load_dotenv(dotenv_path=env_file.as_posix())
        except Exception as e:
            print(t("init_load_failed", error=e))
    existing_languages = os.getenv(constant.LANGUAGES, "python3").split(",")
    existing_problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
    existing_contest_folder = os.getenv(constant.CONTEST_FOLDER, "contest")
    existing_config_str = f"{','.join(existing_languages)}, {existing_problem_folder}, {existing_contest_folder}"

    skip_config = input_until_valid(
        t("init_skip_config", config=existing_config_str),
        allow_all
    )
    if skip_config.lower() != "n":
        languages = existing_languages
        problem_folder = existing_problem_folder
        contest_folder = existing_contest_folder
        print(t("init_skip_confirmed"))
        print(SEPARATE_LINE)

        # Save to .env
        save_config = input_until_valid(
            t("init_save_config"),
            allow_all
        )
        if save_config != "n":
            env_file.touch()  # Ensure file exists
            set_key(env_file.as_posix(), constant.COOKIE, cookie)
            set_key(env_file.as_posix(), constant.PROBLEM_FOLDER, problem_folder)
            set_key(env_file.as_posix(), constant.CONTEST_FOLDER, contest_folder)
            set_key(env_file.as_posix(), constant.LANGUAGES, ",".join(languages))
            set_key(env_file.as_posix(), "PYTHONPATH", ".")
            print(t("init_saved", path=env_file))

            print("\n" + "=" * 50)
            print(t("init_done"))
            print("=" * 50 + "\n")
        else:
            print(t("init_not_saved"))
        print(SEPARATE_LINE)

        return languages, problem_folder, cookie, contest_folder

    # Step 2: Select languages
    print(f"\n{t('init_step2')}")
    lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(SUPPORTED_LANGUAGES))
    pick_languages = input_until_valid(
        t("init_select_lang", options=lang_options),
        lambda x: re.match(r"^[0-5](,[0-5])*$", x),
        t("init_lang_invalid")
    )
    languages = list(set(SUPPORTED_LANGUAGES[int(idx)] for idx in pick_languages.split(",")))
    print(t("init_lang_selected", langs=", ".join(languages)))
    print(SEPARATE_LINE)

    # Step 3: Set problem folder
    print(f"\n{t('init_step3')}")
    input_problem_folder = input_until_valid(
        t("init_problem_folder"),
        allow_all
    )
    problem_folder = input_problem_folder if input_problem_folder else "problems"
    print(t("init_folder_selected", folder=problem_folder))

    input_contest_folder = input_until_valid(
        t("init_contest_folder"),
        allow_all
    )
    contest_folder = input_contest_folder if input_contest_folder else "contest"
    print(t("init_folder_selected", folder=contest_folder))
    print(SEPARATE_LINE)

    # Step 4: Optional notification
    print(f"\n{t('init_step4')}")
    push_key = input_until_valid(
        t("init_push_key"),
        allow_all
    )
    if push_key:
        print(t("init_notify_configured"))
    else:
        print(t("init_notify_skipped"))
    print(SEPARATE_LINE)

    # Save to .env
    save_config = input_until_valid(
        t("init_save_config"),
        allow_all
    )
    if save_config != "n":
        env_file.touch()  # Ensure file exists
        set_key(env_file.as_posix(), constant.COOKIE, cookie)
        set_key(env_file.as_posix(), constant.PROBLEM_FOLDER, problem_folder)
        set_key(env_file.as_posix(), constant.CONTEST_FOLDER, contest_folder)
        set_key(env_file.as_posix(), constant.LANGUAGES, ",".join(languages))
        if push_key:
            set_key(env_file.as_posix(), constant.PUSH_KEY, push_key)
        set_key(env_file.as_posix(), "PYTHONPATH", ".")
        print(t("init_saved", path=env_file))

        print("\n" + "=" * 50)
        print(t("init_done"))
        print("=" * 50 + "\n")
    else:
        print(t("init_not_saved"))
    print(SEPARATE_LINE)

    return languages, problem_folder, cookie, contest_folder


def configure():
    """Main configuration function"""
    env_file = root_path / ".env"

    # Check if .env exists
    if not env_file.exists():
        print(t("init_no_cookie_hint").replace("请确保你已在浏览器中登录 leetcode.cn", "未找到 .env 文件，启动初始化向导..."))
        return initialize_env()

    # Load existing .env
    try:
        load_dotenv(dotenv_path=env_file.as_posix())
    except Exception:
        pass

    print(t("config_title"))
    config_select = input_until_valid(t("config_select"), allow_all)
    print(SEPARATE_LINE)

    if config_select == "2":
        # Re-initialize
        return initialize_env()

    if config_select == "1":
        # Custom config
        lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(SUPPORTED_LANGUAGES))
        pick_languages = input_until_valid(
            t("init_select_lang", options=lang_options),
            lambda x: re.match(r"^[0-5](,[0-5])*$", x),
            t("init_lang_invalid")
        )
        languages = list(set(SUPPORTED_LANGUAGES[int(idx)] for idx in pick_languages.split(",")))
        print(t("init_lang_selected", langs=", ".join(languages)))
        print(SEPARATE_LINE)

        input_problem_folder = input_until_valid(
            t("init_problem_folder"),
            allow_all
        )
        problem_folder = input_problem_folder if input_problem_folder else os.getenv(constant.PROBLEM_FOLDER, "problems")
        print(t("init_folder_selected", folder=problem_folder))
        print(SEPARATE_LINE)

        input_contest_folder = input_until_valid(
            t("init_contest_folder"),
            allow_all
        )
        contest_folder = input_contest_folder if input_contest_folder else os.getenv(constant.CONTEST_FOLDER, "contest")
        print(t("init_folder_selected", folder=contest_folder))
        print(SEPARATE_LINE)

        # Try auto-detect cookie first
        cookie = None
        if HAS_BROWSER_COOKIE:
            auto_detect = input_until_valid(
                t("config_auto_detect"),
                allow_all
            )
            if auto_detect != "n":
                print(t("config_detecting"))
                result = get_browser_cookie()
                if result:
                    cookie, browser_name, cookie_count = result
                    print(t("init_found_cookie", browser=browser_name, count=cookie_count))
                else:
                    print(t("config_no_browser_cookie"))
                print(SEPARATE_LINE)

        if not cookie:
            cookie = read_cookie_from_file()
            if not cookie:
                input_cookie = input_until_valid(
                    t("config_enter_cookie"),
                    allow_all
                )
                cookie = input_cookie.strip() if input_cookie else os.getenv(constant.COOKIE)

        cookie = check_and_update_cookie(cookie)
        print(SEPARATE_LINE)

        update_config = input_until_valid(
            t("config_update_env"),
            allow_all
        )
        if update_config == "y":
            with env_file.open("w") as f:
                f.write(f'{constant.COOKIE}="{cookie}"\n')
                f.write(f'{constant.PROBLEM_FOLDER}="{problem_folder}"\n')
                f.write(f'{constant.CONTEST_FOLDER}="{contest_folder}"\n')
                f.write(f'{constant.LANGUAGES}="{",".join(languages)}"\n')
            print(t("config_env_updated", path=env_file))
        print(SEPARATE_LINE)
    else:
        # Load from .env
        cookie = check_and_update_cookie(os.getenv(constant.COOKIE))
        problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        contest_folder = os.getenv(constant.CONTEST_FOLDER, "contest")
        languages = os.getenv(constant.LANGUAGES, "python3").split(",")
        print(t("init_lang_selected", langs=", ".join(languages)))
        print(t("init_folder_selected", folder=problem_folder))
        print(t("init_folder_selected", folder=contest_folder))
        print(SEPARATE_LINE)

    logging.basicConfig(level=logging.ERROR)
    return languages, problem_folder, cookie, contest_folder


# ============================================================================
# Problem Management
# ============================================================================

def get_problem(languages, problem_folder, cookie):
    """Get problem menu handler"""
    while True:
        get_problem_method = input_until_valid(
            t("get_menu"),
            allow_all
        )
        print(SEPARATE_LINE)
        match get_problem_method:
            case "1":
                exit_code = daily_auto_main(problem_folder, cookie, languages)
                if exit_code == 0:
                    print(t("get_daily_success"))
                else:
                    print(t("get_daily_failed"))
            case "2":
                input_problem_id = input_until_valid(
                    t("get_problem_id"), allow_all_not_empty, t("get_problem_id_empty")
                )
                problem_id = back_question_id(input_problem_id)
                exit_code = get_problem_main(
                    problem_id, force=True, cookie=cookie, replace_problem_id=True, skip_language=True,
                    languages=languages, problem_folder=problem_folder
                )
                if exit_code == 0:
                    print(t("get_success", id=problem_id))
                else:
                    print(t("get_failed", id=problem_id))
            case "3":
                exit_code = lucky_main(languages, problem_folder)
                if exit_code == 0:
                    print(t("get_random_success"))
                else:
                    print(t("get_random_failed"))
            case "4":
                exit_code = remain_main(cookie, languages, problem_folder)
                if exit_code == 0:
                    print(t("get_random_success"))
                else:
                    print(t("get_remain_failed"))
            case "5":
                _handle_category_selection(languages, problem_folder, cookie)
            case "6":
                _handle_contest_problem(languages, problem_folder, cookie)
            case _:
                return


def _handle_category_selection(languages, problem_folder, cookie):
    """Handle category-based problem selection"""
    tags = root_path / "data" / "tags.json"
    if not tags.exists():
        print(t("tags_not_found"))
        return
    with tags.open("r", encoding="utf-8") as f:
        json_tags = json.load(f)
    tags_list = list(json_tags.keys())
    pick_tag = input_pick_array("tag", tags_list)
    if pick_tag is None:
        return
    tag = tags_list[pick_tag]
    tag_data = json_tags[tag]
    print(t("tag_selected", tag=tag, translations=",".join(tag_data.get('translations', []))))
    print(SEPARATE_LINE)
    problems = tag_data.get("problems", [])
    if not problems:
        print(t("tag_no_problems"))
        return
    pick_problem = input_pick_array("problem", problems)
    if pick_problem is None:
        return
    problem_id = problems[pick_problem]
    exit_code = get_problem_main(
        problem_id, force=True, cookie=cookie, replace_problem_id=True, skip_language=True,
        languages=languages, problem_folder=problem_folder
    )
    if exit_code == 0:
        print(t("get_success", id=problem_id))
    else:
        print(t("get_failed", id=problem_id))


def _handle_contest_problem(languages, problem_folder, cookie):
    """Handle contest-based problem fetching"""
    contest_type = input_until_valid(
        t("contest_type_menu"),
        lambda x: x in ["0", "1", "2"],
        t("contest_invalid_type")
    )
    print(SEPARATE_LINE)
    if contest_type == "0":
        return
    contest_id = input_until_valid(
        t("contest_id_num"),
        allow_number,
        t("contest_id_empty")
    )
    print(SEPARATE_LINE)
    if contest_type == "1":
        contest_id = f"weekly-contest-{contest_id}"
    elif contest_type == "2":
        contest_id = f"biweekly-contest-{contest_id}"
    else:
        print(t("contest_invalid_type"))
        return
    contest_questions = contest_lib.get_contest_info(contest_id)
    results = []
    with ThreadPoolExecutor(max_workers=max(1, len(contest_questions))) as executor:
        for question_data in contest_questions:
            results.append(
                executor.submit(get_problem_main, problem_slug=question_data["title_slug"], force=True,
                                cookie=cookie, skip_language=True,
                                languages=languages, problem_folder=problem_folder))
    for future in results:
        exit_code = future.result()
        if exit_code != 0:
            print(t("get_failed", id="contest problem"))


def change_problem(languages, problem_folder):
    """Change test problem for all languages"""
    input_problem_id = input_until_valid(
        t("get_problem_id"), allow_all_not_empty, t("get_problem_id_empty")
    )
    problem_id = back_question_id(input_problem_id)
    for lang in languages:
        cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
        if not cls:
            print(t("lang_not_support", lang=lang))
            continue
        obj: lc_libs.LanguageWriter = cls()
        obj.change_test(root_path, problem_folder, format_question_id(problem_id))
        print(t("change_test_success", lang=lang, id=problem_id))
    print(SEPARATE_LINE)


# ============================================================================
# Submission
# ============================================================================

def submit(languages, problem_folder, cookie):
    """Submit code menu handler"""
    while True:
        submit_method = input_until_valid(
            t("submit_menu"),
            allow_all
        )
        print(SEPARATE_LINE)
        if submit_method == "2" or submit_method == "4":
            lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(SUPPORTED_LANGUAGES))
            language_select = input_until_valid(
                t("init_select_lang", options=lang_options),
                lambda x: re.match(r"^[0-5](,[0-5])*$", x),
                t("init_lang_invalid")
            )
            languages = list(set(SUPPORTED_LANGUAGES[int(idx)] for idx in language_select.split(",")))
            print(SEPARATE_LINE)
        match submit_method:
            case "1" | "2":
                daily_info = get_daily_question()
                if not daily_info:
                    print(t("submit_daily_failed"))
                    continue
                problem_id = daily_info['questionId']
            case "3" | "4":
                input_problem_id = input_until_valid(
                    t("get_problem_id"), allow_all_not_empty, t("get_problem_id_empty")
                )
                problem_id = back_question_id(input_problem_id)
            case _:
                return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        print(t("submit_starting"))
        logging.basicConfig(level=logging.INFO, force=True)
        for i, lang in enumerate(languages):
            print(t("submit_in_lang", lang=lang))
            loop.run_until_complete(
                submit_main_async(
                    root_path,
                    format_question_id(problem_id),
                    lang,
                    cookie,
                    problem_folder
                )
            )
            if i < len(languages) - 1:
                time.sleep(1)
        if loop.is_running():
            loop.stop()
        loop.close()
        logging.basicConfig(level=logging.ERROR, force=True)
        time.sleep(1)
        print(t("submit_done"))
        print(SEPARATE_LINE)


# ============================================================================
# Contest Management
# ============================================================================

def contest_main(languages, contest_folder, cookie):
    """Contest menu handler"""
    def contest_list():
        cur_page = 1
        while True:
            contest_page = contest_lib.get_contest_list(cur_page)
            total, data, has_more = contest_page["total"], contest_page["contests"], contest_page["has_more"]
            max_page = math.ceil(total / 10)
            if not data:
                print(t("contest_no_contests"))
                break
            contest_content = "\n".join(
                f"{_i}. [{datetime.datetime.fromtimestamp(c['start_time']).strftime('%Y-%m-%d %H:%M:%S')}]{c['title']}"
                for _i, c in enumerate(data, start=1))
            user_input_select = input_until_valid(
                t("contest_page", total=total, content=contest_content),
                allow_all
            )
            pick = None
            match user_input_select:
                case "b":
                    cur_page = max(1, cur_page - 1)
                case "n":
                    cur_page = min(max_page, cur_page + 1)
                case v if v.isdigit() and 1 <= int(v) <= 10:
                    pick = int(v)
                case _:
                    break
            print(SEPARATE_LINE)
            if not pick:
                continue
            return data[pick - 1]
        return None

    user_input_contest = input_until_valid(
        t("contest_menu"),
        allow_all
    )
    print(SEPARATE_LINE)
    match user_input_contest:
        case "1":
            contest = contest_list()
            if not contest:
                return None
            contest_id = contest["title_slug"]
        case "2":
            contest_id = input_until_valid(
                t("contest_id"),
                allow_all_not_empty,
                t("contest_id_empty")
            )
        case _:
            return None

    contest_questions = contest_lib.get_contest_info(contest_id)
    p = root_path / contest_folder / contest_id
    p.mkdir(parents=True, exist_ok=True)

    def process_question_worker(question_idx_data_tuple):
        question_idx, question_data = question_idx_data_tuple
        question_slug = question_data["title_slug"]

        subp = p / chr(ord('a') + question_idx - 1)
        subp.mkdir(parents=True, exist_ok=True)

        problem_info = contest_lib.get_contest_problem_info(contest_id, question_slug, ["python3"], cookie)

        if not problem_info:
            logging.error(f"Failed to get contest [{contest_id}] problem [{question_slug}]")
            return False

        try:
            with (subp / "problem.md").open("w", encoding="utf-8") as f:
                f.write(problem_info["en_markdown_content"])
            with (subp / "problem_zh.md").open("w", encoding="utf-8") as f:
                f.write(problem_info["cn_markdown_content"])
            with (subp / "input.json").open("w", encoding="utf-8") as f:
                json.dump(problem_info["question_example_testcases"], f)
            with (subp / "output.json").open("w", encoding="utf-8") as f:
                json.dump(problem_info["question_example_testcases_output"], f)

            for lang, code_content in problem_info["language_default_code"].items():
                cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
                if not cls:
                    logging.warning(f"Unsupported language {lang} for question {question_slug}")
                    continue
                obj: lc_libs.LanguageWriter = cls()
                solution_file = obj.solution_file
                with (subp / solution_file).open("w", encoding="utf-8") as f:
                    generated_code = obj.write_contest(code_content, problem_info["question_id"], "")
                    if not generated_code:
                        logging.warning(f"Failed to write solution for {lang} for question {question_slug}")
                        continue
                    f.write(generated_code)
            logging.info(f"Successfully processed question {question_slug}")
            return True
        except Exception as e:
            logging.error(f"Error writing files for question {question_slug}: {e}")
            return False

    num_workers = max(1, len(contest_questions))
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        tasks_data = list(enumerate(contest_questions, start=1))
        results = list(executor.map(process_question_worker, tasks_data))

        for result in results:
            if not result:
                print(t("get_failed", id="contest question"))
                p.rmdir()
                return None

    print(t("contest_generated", id=contest_id))
    print(SEPARATE_LINE)
    return None


# ============================================================================
# Favorite Management
# ============================================================================

def favorite_main(languages, problem_folder, cookie):
    """Favorite menu handler"""
    def favorite_list():
        while True:
            my_favorites = query_my_favorites(cookie)
            total, data, has_more = my_favorites["total"], my_favorites["favorites"], my_favorites["has_more"]
            if not data:
                print(t("fav_no_favorites"))
                break
            content = "\n".join(
                [f"{_i}. {f['name']}" for _i, f in enumerate(data, start=1)],
            )
            user_input_select = input_until_valid(
                t("contest_page", total=total, content=content),
                allow_all
            )
            pick = None
            match user_input_select:
                case v if v.isdigit() and 1 <= int(v) <= 10:
                    pick = int(v)
                case _:
                    break
            print(SEPARATE_LINE)
            if not pick:
                continue
            return data[pick - 1]
        return None

    def question_list(favorite_slug):
        def question_to_str(q):
            difficulty = constant.DIFFICULTY_TRANSLATE_MAP.get(q["difficulty"], "未知")
            status = constant.STATUS_TRANSLATE_MAP.get(q["status"], "x")
            paid_only = " {会员}" if q["paid_only"] else ""
            return f"{status} [{q['question_frontend_id']}] {q['translated_title']} ({difficulty}){paid_only}"

        cur_page = 1
        page_size = 20
        while True:
            _questions = query_favorite_questions(favorite_slug, cookie, limit=page_size,
                                                  skip=(cur_page - 1) * page_size)
            total, data, has_more = _questions["total"], _questions["questions"], _questions["has_more"]
            max_page = math.ceil(total / page_size)
            if not data:
                print(t("fav_no_questions"))
                break
            content = "\n".join(
                [f"{_i}. {question_to_str(q)}" for _i, q in enumerate(data, start=1)],
            )
            user_input_select = input_until_valid(
                t("contest_page", total=total, content=content),
                allow_all
            )
            pick = None
            match user_input_select:
                case "b":
                    cur_page = max(1, cur_page - 1)
                case "n":
                    cur_page = min(max_page, cur_page + 1)
                case v if v.isdigit() and 1 <= int(v) <= page_size:
                    pick = int(v)
                case _:
                    break
            print(SEPARATE_LINE)
            if not pick:
                continue
            return data[pick - 1]
        return None

    if check_cookie_expired(cookie):
        print(t("fav_expired"))
        return
    while True:
        favorite = favorite_list()
        if not favorite:
            return
        slug = favorite["slug"]
        while True:
            favorite_method = input_until_valid(
                t("fav_menu"),
                allow_all
            )
            print(SEPARATE_LINE)
            match favorite_method:
                case "1":
                    question = question_list(slug)
                    if not question:
                        break
                    code = get_problem_main(
                        problem_slug=question["title_slug"], force=True, cookie=cookie, replace_problem_id=True,
                        skip_language=True, languages=languages, problem_folder=problem_folder
                    )
                    if code == 0:
                        print(t("get_success", id=f"{question['question_frontend_id']} {question['translated_title']}"))
                    else:
                        print(t("get_failed", id=f"{question['question_frontend_id']} {question['translated_title']}"))
                case "2":
                    input_questions = input_until_valid(
                        t("fav_add_ids"),
                        allow_all_not_empty,
                        t("fav_ids_empty")
                    )
                    question_ids = [q.strip() for q in input_questions.split(",")]
                    if not question_ids:
                        print(t("fav_ids_empty"))
                        continue
                    with ThreadPoolExecutor() as executor:
                        slugs = list(executor.map(get_question_slug_by_id, question_ids, [cookie] * len(question_ids)))

                    questions = []
                    for question_id, question_slug in zip(question_ids, slugs):
                        if not question_slug:
                            print(f"Invalid question ID: {question_id}. Skipping.")
                            continue
                        questions.append(question_slug)
                    if not questions:
                        print(t("fav_ids_empty"))
                        continue
                    result = batch_add_questions_to_favorite(slug, questions, cookie)
                    if result.get("status") == "success":
                        print(t("fav_add_success", count=len(questions), name=favorite['name']))
                    else:
                        print(t("fav_add_failed", name=favorite['name'], msg=result.get('message')))
                case _:
                    break


def link_problems(problem_folder):
    """Link two problems with identical solutions"""
    target_id = input_until_valid(
        t("link_target_id"), allow_all_not_empty, t("get_problem_id_empty")
    )
    target_id = back_question_id(target_id)

    source_id = input_until_valid(
        t("link_source_id"), allow_all_not_empty, t("get_problem_id_empty")
    )
    source_id = back_question_id(source_id)

    reason = input_until_valid(
        t("link_reason"), allow_all
    )

    delete_solution = input_until_valid(
        t("link_delete_solution"), allow_all
    )

    print(SEPARATE_LINE)

    try:
        link_file = create_link(
            target_problem=target_id,
            source_problem=source_id,
            reason=reason if reason else None,
            source_folder=problem_folder,
            target_folder=problem_folder
        )
        print(t("link_success", target=target_id, source=source_id))

        if delete_solution == "y":
            target_path = root_path / problem_folder / f"{problem_folder}_{target_id}"
            solution_files = ["solution.py", "solution.go", "Solution.java", "Solution.cpp", "solution.rs", "solution.ts", "Cargo.toml"]
            for sol_file in solution_files:
                file_path = target_path / sol_file
                if file_path.exists():
                    file_path.unlink()
                    print(f"Deleted: {sol_file}")

    except Exception as e:
        print(t("link_failed", msg=str(e)))

    print(SEPARATE_LINE)


def _get_problem_slug_from_id(problem_id: str, cookie: str) -> Optional[str]:
    """通过题目 ID 获取 problem_slug"""
    origin_problem_id = back_question_id(problem_id)
    questions = lc_libs.get_questions_by_key_word(origin_problem_id, cookie)
    if not questions:
        return None
    for question in questions:
        if question["questionFrontendId"] == origin_problem_id:
            return question["titleSlug"]
    return None


def _display_width(s: str) -> int:
    """计算字符串在终端的显示宽度（中文等宽字符占两列）"""
    import unicodedata
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in s)


def _pad_to_width(s: str, width: int) -> str:
    """将字符串填充到指定显示宽度"""
    current_width = _display_width(s)
    if current_width >= width:
        return s
    return s + ' ' * (width - current_width)


def _display_solution_detail(title: str, author_name: str, upvote: int,
                              content: str, solution_link: str) -> bool:
    """
    展示题解详情（边界框 + 分页器）

    Returns:
        True 如果用户选择保存，False 否则
    """
    # 边界框展示元信息（固定宽度 50）
    box_width = 50
    content_width = box_width - 4  # 去掉 "│ " 和 " │"

    print(f"\n┌{'─' * (box_width - 2)}┐")

    # 标题行（截断并填充）
    title_display = title[:content_width - 2] if _display_width(title) > content_width - 2 else title
    print(f"│ 📄 {_pad_to_width(title_display, content_width - 2)}│")

    # 作者行
    author_display = author_name[:content_width - 2] if _display_width(author_name) > content_width - 2 else author_name
    print(f"│ 👤 {_pad_to_width(author_display, content_width - 2)}│")

    # 点赞行
    upvote_str = str(upvote)
    print(f"│ 👍 {_pad_to_width(upvote_str, content_width - 2)}│")

    # 链接行（如果有）
    if solution_link:
        link_display = solution_link[:content_width - 2] if len(solution_link) > content_width - 2 else solution_link
        print(f"│ 🔗 {_pad_to_width(link_display, content_width - 2)}│")

    print(f"└{'─' * (box_width - 2)}┘")

    # 使用分页器展示内容
    if content:
        import subprocess
        import tempfile
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"> Author: {author_name} | Upvotes: {upvote}\n\n")
                f.write(content)
                tmp_path = f.name

            # 使用列表形式避免 shell 注入
            import shlex
            pager_cmd = shlex.split(os.environ.get('PAGER', 'less -R'))
            subprocess.run(pager_cmd + [tmp_path])
        except Exception:
            # 如果分页器失败，直接打印前 100 行
            print("\n" + SEPARATE_LINE)
            lines = content.split('\n')
            for line in lines[:100]:
                print(line)
            if len(lines) > 100:
                print(f"\n... (共 {len(lines)} 行，已截断)")
            print(SEPARATE_LINE)
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.unlink(tmp_path)

    save_input = input_until_valid(t("solution_save"), allow_all)
    return save_input.lower() == "y"


def _save_solution(article_content: dict, problem_folder: str, problem_id: str):
    """保存题解到本地文件"""
    problem_dir = root_path / problem_folder / f"{problem_folder}_{back_question_id(problem_id)}"
    if not problem_dir.exists():
        print(f"{t('solution_save_failed')} - 目录不存在: {problem_dir}")
        return
    author_info = article_content.get("author", {})
    profile = author_info.get("profile", {})
    author_slug = profile.get("userSlug", "unknown") if profile else "unknown"
    # Sanitize author_slug: only allow alphanumeric, underscore, dash
    author_slug = re.sub(r"[^a-zA-Z0-9_-]", "", author_slug) or "unknown"
    save_path = problem_dir / f"solution_{author_slug}.md"
    author_name = profile.get("realName", "") or author_info.get("username", "")
    title = article_content.get("title", "")
    content = article_content.get("content", "")
    upvote = article_content.get("upvoteCount", 0)
    md = f"# {title}\n\n> Author: {author_name}\n> Upvotes: {upvote}\n\n---\n\n{content}"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(t("solution_saved", path=save_path))


def _browse_community_solutions(cookie: str, problem_folder: str):
    """浏览社区题解（支持分页）"""
    problem_id_input = input_until_valid(t("solution_enter_problem_id"), allow_all_not_empty,
                                          t("solution_problem_id_empty"))
    print(SEPARATE_LINE)
    if not problem_id_input:
        return

    problem_slug = _get_problem_slug_from_id(problem_id_input, cookie)
    if not problem_slug:
        print(t("solution_no_articles"))
        return

    page_size = 10
    cur_page = 1

    while True:
        print(t("solution_fetching"))
        result = lc_libs.get_answer_articles(problem_slug, cookie, first=page_size, skip=(cur_page - 1) * page_size)
        total = result.get("total", 0)
        articles = result.get("articles", [])

        if not articles:
            print(t("solution_no_articles"))
            return

        max_page = math.ceil(total / page_size)
        # 构建题解列表展示
        lines = []
        for i, article in enumerate(articles, 1):
            title = article.get("title", "")
            author_info = article.get("author", {})
            profile = author_info.get("profile", {})
            author_name = profile.get("realName", "") or author_info.get("username", "?")
            upvote = article.get("upvoteCount", 0)
            topic_id = article.get("topic", {}).get("id", "")
            article_slug = article.get("slug", "")
            solution_link = f"https://leetcode.cn/problems/{problem_slug}/solutions/{topic_id}/{article_slug}/" if topic_id and article_slug else ""
            lines.append(f"  {i}. {title}")
            lines.append(f"     👤{author_name} | 👍{upvote}")
            if solution_link:
                lines.append(f"     🔗 {solution_link}")
        content = "\n".join(lines)

        select = input_until_valid(
            t("solution_page", total=total, page=cur_page, max_page=max_page, content=content),
            allow_all
        )

        pick = None
        match select:
            case "" | "0":
                # 回车或 0 返回
                return
            case "b":
                if cur_page == 1:
                    print(t("solution_first_page"))
                else:
                    cur_page = max(1, cur_page - 1)
            case "n":
                if cur_page == max_page:
                    print(t("solution_last_page"))
                else:
                    cur_page = min(max_page, cur_page + 1)
            case v if v.isdigit() and 1 <= int(v) <= len(articles):
                pick = int(v)
            case _:
                # 其他无效输入，继续显示当前页
                continue

        print(SEPARATE_LINE)
        if not pick:
            continue

        article = articles[pick - 1]
        slug = article.get("slug")
        uuid = article.get("uuid", "")
        if not slug:
            continue

        print(t("solution_loading_detail"))
        from python.lc_libs.solution_article import get_solution_content
        detail = get_solution_content(slug, cookie)
        if detail:
            title = detail.get("title", "")
            author_info = detail.get("author", {})
            profile = author_info.get("profile", {})
            author_name = profile.get("realName", "") or author_info.get("username", "?")
            upvote = detail.get("upvoteCount", 0)
            content = detail.get("content", "")
            solution_link = f"https://leetcode.cn/problems/{problem_slug}/solutions/{uuid}/" if uuid else ""

            if _display_solution_detail(title, author_name, upvote, content, solution_link):
                _save_solution(detail, problem_folder, problem_id_input)
        else:
            print(t("solution_no_articles"))
        print(SEPARATE_LINE)


def _view_author_solutions(cookie: str, problem_folder: str):
    """查看指定作者题解"""
    author_input = input_until_valid(t("solution_enter_author"), allow_all)
    author_slug = author_input.strip() if author_input.strip() else "endlesscheng"
    print(SEPARATE_LINE)

    problem_id_input = input_until_valid(t("solution_enter_problem_id"), allow_all_not_empty,
                                          t("solution_problem_id_empty"))
    if not problem_id_input:
        return

    problem_slug = _get_problem_slug_from_id(problem_id_input, cookie)
    if not problem_slug:
        print(t("solution_no_articles"))
        return

    print(t("solution_fetching"))
    from python.lc_libs.solution_article import get_solution_by_author
    detail = get_solution_by_author(problem_slug, author_slug, cookie)
    if not detail:
        print(t("solution_author_not_found"))
        return

    author_info = detail.get("author", {})
    profile = author_info.get("profile", {})
    author_name = profile.get("realName", "") or author_info.get("username", "?")
    title = detail.get("title", "")
    upvote = detail.get("upvoteCount", 0)
    uuid = detail.get("uuid", "")
    content = detail.get("content", "")
    solution_link = f"https://leetcode.cn/problems/{problem_slug}/solutions/{uuid}/" if uuid else ""

    if _display_solution_detail(title, author_name, upvote, content, solution_link):
        _save_solution(detail, problem_folder, problem_id_input)
    print(SEPARATE_LINE)


def solution_center(cookie, problem_folder):
    """题解中心"""
    while True:
        method = input_until_valid(t("solution_menu"), allow_all)
        print(SEPARATE_LINE)
        match method:
            case "1":
                # 拉取我的题解
                user_slug = os.getenv("LEETCODE_USER", "")
                if not user_slug:
                    print(t("fetch_no_user"))
                    print(SEPARATE_LINE)
                    continue
                fetch_method = input_until_valid(t("fetch_menu"), allow_all)
                print(SEPARATE_LINE)
                match fetch_method:
                    case "1":
                        fetch_solution_main(dry_run=True, user_slug=user_slug,
                                            problem_folder=problem_folder, cookie=cookie)
                    case "2":
                        force_input = input_until_valid(t("fetch_force"), allow_all)
                        force = force_input.lower() == "y"
                        delay_input = input_until_valid(t("fetch_delay"), allow_all)
                        delay = float(delay_input) if delay_input else 3.0
                        print(SEPARATE_LINE)
                        print(t("fetch_running"))
                        fetch_solution_main(dry_run=False, force=force, delay=delay,
                                            user_slug=user_slug, problem_folder=problem_folder, cookie=cookie)
                        print(t("fetch_done"))
                    case "3":
                        pid_input = input_until_valid(t("fetch_problem_id"), allow_all)
                        if not pid_input:
                            continue
                        force_input = input_until_valid(t("fetch_force"), allow_all)
                        force = force_input.lower() == "y"
                        print(SEPARATE_LINE)
                        print(t("fetch_running"))
                        fetch_solution_main(dry_run=False, force=force, problem_id=pid_input,
                                            user_slug=user_slug, problem_folder=problem_folder, cookie=cookie)
                        print(t("fetch_done"))
                    case _:
                        pass
                print(SEPARATE_LINE)
            case "2":
                _browse_community_solutions(cookie, problem_folder)
            case "3":
                _view_author_solutions(cookie, problem_folder)
            case _:
                return


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    """Main entry point"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="LeetCode 工具集")
    parser.add_argument('--en', action='store_true', help='Use English interface')
    parser.add_argument('--init', action='store_true', help='Force initialization wizard')
    args = parser.parse_args()

    # Set language
    if args.en:
        set_language("en")

    try:
        if args.init:
            languages, problem_folder, cookie, contest_folder = initialize_env()
        else:
            languages, problem_folder, cookie, contest_folder = configure()

        while True:
            main_function = input_until_valid(
                t("main_menu"),
                allow_all
            )
            print(SEPARATE_LINE)
            match main_function:
                case "1":
                    get_problem(languages, problem_folder, cookie)
                case "2":
                    submit(languages, problem_folder, cookie)
                case "3":
                    change_problem(languages, problem_folder)
                case "4":
                    contest_main(languages, contest_folder, cookie)
                case "5":
                    clean_empty_java_main(root_path, problem_folder)
                    print(t("clean_done"))
                    print(SEPARATE_LINE)
                case "6":
                    clean_error_rust_main(root_path, problem_folder)
                    print(t("clean_done"))
                    print(SEPARATE_LINE)
                case "7":
                    favorite_main(languages, problem_folder, cookie)
                    print(SEPARATE_LINE)
                case "8":
                    link_problems(problem_folder)
                case "9":
                    solution_center(cookie, problem_folder)
                case _:
                    print(t("main_exit"))
                    break
    except KeyboardInterrupt:
        print(f"\n{t('main_bye')}")


if __name__ == '__main__':
    main()
    sys.exit()
