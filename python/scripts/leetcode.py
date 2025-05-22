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

from pathlib import Path
from dotenv import load_dotenv

file_path = Path(__file__)
root_path = file_path.parent.parent.parent
sys.path.insert(0, root_path.as_posix())

from python.constants import constant
from python.lc_libs import get_daily_question, contest as contest_lib
import python.lc_libs as lc_libs
from python.scripts.submit import main as submit_main_async
from python.utils import back_question_id, format_question_id, check_cookie_expired
from python.scripts.daily_auto import main as daily_auto_main
from python.scripts.get_problem import main as get_problem_main
from python.scripts.tools import lucky_main, remain_main, clean_empty_java_main, clean_error_rust_main

__separate_line = "-" * 50

__user_input_config = """Please select the configuration [0-1, default: 0]:
0. Load default config from .env
1. Custom config
"""
__user_input_function = """Please select the main function [0-5, default: 0]:
0. Exit
1. Get problem
2. Submit
3. Change test problem
4. Contest
5. Clean empty java
6. Clean error rust
"""
__user_input_get_problem = """Please select the get problem method [0-5, default: 0]:
0. Back
1. Daily auto
2. Specified problem ID
3. Random
4. Random remain [Problems that submitted but not accepted yet]
5. Category
"""
__user_input_submit = """Please select the submit method [0-4, default: 0]:
0. Back
1. Daily submit[All selected languages]
2. Daily submit[Select language]
3. Submit specified problem[All selected languages]
4. Submit specified problem[Select language]
"""
__user_input_problem_id = "Enter the problem ID (e.g. 1, LCR 043, 面试题 01.01, etc.): "
__user_input_contest = """Please select the contest method [0-2, default: 0]:
0. Back
1. List contests
2. Contest by slug
"""
__user_input_contest_id = "Enter the contest ID (e.g. biweekly-contest-155, etc.): "
__user_input_page = """Total of [{}] elements, please enter [default: 0]:
0. Back
{}

b. last page
n. next page
"""

__supported_languages = ["python3", "java", "golang", "cpp", "typescript", "rust"]
__user_input_language = f"""Select multiple languages you want to use, separated by comma [0-{len(__supported_languages) - 1}, default: 0]:
{"\n".join(f"{idx}. {lang}" for idx, lang in enumerate(__supported_languages))}
"""

__allow_all = lambda x: True
__allow_all_not_empty = lambda x: bool(x.strip())


def input_until_valid(prompt, check_func, error_msg=None):
    while True:
        user_input = input(prompt)
        if check_func(user_input):
            return user_input
        elif error_msg:
            print(error_msg)
        print(__separate_line)


def input_pick_array(desc, arr):
    user_input = input_until_valid(
        f"Enter the number of the {desc} [1-{len(arr)}, or 0 to go back (default), or input random to random: "
        f"0. Back\n{'\n'.join(f'{i}. {v}' for i, v in enumerate(arr, 1))}\n",
        __allow_all
    )
    if user_input == "0":
        return None
    if user_input == "random":
        return random.randint(0, len(arr) - 1)
    try:
        pick = int(user_input) - 1
        if pick < 0 or pick >= len(arr):
            pick = random.randint(0, len(arr) - 1)
        return pick
    except ValueError:
        return None


def configure():
    def check_and_update_cookie(_cookie: str) -> str:
        while check_cookie_expired(_cookie):
            update_cookie = input_until_valid(
                "Cookie might expired, do you want to update it? [y/n, default: n]: ",
                __allow_all
            )
            if update_cookie == "y":
                _cookie = input_until_valid(
                    "Enter your LeetCode cookie: ",
                    __allow_all
                )
                print("Cookie updated.")
                print(__separate_line)
            else:
                print(__separate_line)
                break
        return _cookie

    print("Setting up the environment...")
    config_select = input_until_valid(__user_input_config, __allow_all)
    print(__separate_line)
    env_file = root_path / ".env"

    try:
        load_dotenv(dotenv_path=env_file.as_posix())
    except Exception:
        pass
    if config_select == "1":
        pick_languages = input_until_valid(
            __user_input_language,
            lambda x: re.match(r"^[0-5](,[0-5])*$", x),
            "Invalid input, please enter a comma-separated list of numbers from 0 to 5."
        )
        languages = list(set(__supported_languages[int(idx)] for idx in pick_languages.split(",")))
        print(f"Languages selected: {', '.join(languages)}")
        print(__separate_line)

        input_problem_folder = input_until_valid(
            "Enter the problem folder path (press enter to use default): ",
            __allow_all
        )
        if input_problem_folder:
            problem_folder = input_problem_folder
        else:
            problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        print(f"Problem folder selected: {problem_folder}")
        print(__separate_line)

        input_contest_folder = input_until_valid(
            "Enter the contest folder path (press enter to use default): ",
            __allow_all
        )
        if input_contest_folder:
            contest_folder = input_contest_folder
        else:
            contest_folder = os.getenv(constant.CONTEST_FOLDER, "contest")
        print("Contest folder selected: ", contest_folder)
        print(__separate_line)

        input_cookie = input_until_valid(
            "Enter your LeetCode cookie (press enter to use default): ",
            __allow_all
        )
        if input_cookie:
            cookie = input_cookie.strip()
        else:
            cookie = os.getenv(constant.COOKIE)
        cookie = check_and_update_cookie(cookie)
        print(__separate_line)

        update_config = input_until_valid(
            "Do you want to update the .env file with this configuration? [y/n, default: n]: ",
            __allow_all
        )
        if update_config == "y":
            with env_file.open("w") as f:
                f.write(f"{constant.COOKIE}={cookie}\n")
                f.write(f"{constant.PROBLEM_FOLDER}={problem_folder}\n")
                f.write(f"{constant.LANGUAGES}={','.join(languages)}\n")
            print(f"Updated {env_file} with the new configuration.")
        print(__separate_line)
    else:
        cookie = check_and_update_cookie(os.getenv(constant.COOKIE))
        problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        contest_folder = os.getenv(constant.CONTEST_FOLDER, "contest")
        languages = os.getenv(constant.LANGUAGES, "python3").split(",")
        print(f"Languages selected: {', '.join(languages)}")
        print(f"Problem folder selected: {problem_folder}")
        print(f"Contest folder selected: {contest_folder}")
        print(__separate_line)

    logging.basicConfig(level=logging.ERROR)
    return languages, problem_folder, cookie, contest_folder


def get_problem(languages, problem_folder, cookie):
    while True:
        get_problem_method = input_until_valid(
            __user_input_get_problem,
            __allow_all
        )
        print(__separate_line)
        match get_problem_method:
            case "1":
                exit_code = daily_auto_main(problem_folder, cookie, languages)
                if exit_code == 0:
                    print("Daily auto completed successfully.")
                else:
                    print("Daily auto failed.")
            case "2":
                input_problem_id = input_until_valid(
                    __user_input_problem_id, __allow_all_not_empty, "Problem ID cannot be empty."
                )
                problem_id = back_question_id(input_problem_id)
                exit_code = get_problem_main(problem_id, cookie=cookie, replace_problem_id=True,
                                             languages=languages, problem_folder=problem_folder)
                if exit_code == 0:
                    print(f"Problem [{problem_id}] fetched successfully.")
                else:
                    print(f"Failed to fetch the problem. Make sure the problem ID is correct: {problem_id}")
            case "3":
                exit_code = lucky_main(languages, problem_folder)
                if exit_code == 0:
                    print("Random problem fetched successfully.")
                else:
                    print("Failed to fetch a random problem. Please try again.")
            case "4":
                exit_code = remain_main(cookie, languages, problem_folder)
                if exit_code == 0:
                    print("Random remaining problem fetched successfully.")
                else:
                    print("Failed to fetch a random remaining problem."
                          "Cookie may be invalid, or no remaining problems.")
            case "5":
                tags = root_path / "data" / "tags.json"
                if not tags.exists():
                    print("Tags file not found. Please contact the author.")
                    continue
                with tags.open("r", encoding="utf-8") as f:
                    json_tags = json.load(f)
                tags = list(json_tags.keys())
                pick_tag = input_pick_array("tag", tags)
                if pick_tag is None:
                    continue
                tag = tags[pick_tag]
                tag_data = json_tags[tag]
                print(f"Selected tag: {tag} [{','.join(tag_data.get('translations', []))}]")
                print(__separate_line)
                problems = tag_data.get("problems", [])
                if not problems:
                    print("No problems found for this tag.")
                    continue
                pick_problem = input_pick_array("problem", problems)
                if pick_problem is None:
                    continue
                problem_id = problems[pick_problem]
                exit_code = get_problem_main(problem_id, cookie=cookie, replace_problem_id=True,
                                             languages=languages, problem_folder=problem_folder)
                if exit_code == 0:
                    print(f"Problem [{problem_id}] fetched successfully.")
                else:
                    print(f"Failed to fetch the problem. Check {problem_id} is correct?")
            case _:
                return


def submit(languages, problem_folder, cookie):
    while True:
        submit_method = input_until_valid(
            __user_input_submit,
            __allow_all
        )
        print(__separate_line)
        if submit_method == "2" or submit_method == "4":
            language_select = input_until_valid(
                __user_input_language,
                lambda x: re.match(r"^[0-5](,[0-5])*$", x),
                "Invalid input, please enter a comma-separated list of numbers from 0 to 5."
            )
            languages = list(set(__supported_languages[int(idx)] for idx in language_select.split(",")))
            print(__separate_line)
        match submit_method:
            case "1" | "2":
                daily_info = get_daily_question()
                if not daily_info:
                    print(f"Unable to get daily question, possibly network issue?")
                    continue
                problem_id = daily_info['questionId']
            case "3" | "4":
                input_problem_id = input_until_valid(
                    __user_input_problem_id, __allow_all_not_empty, "Problem ID cannot be empty."
                )
                problem_id = back_question_id(input_problem_id)
            case _:
                return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        print("Starting submission, please wait...")
        logging.basicConfig(level=logging.INFO, force=True)
        for i, lang in enumerate(languages):
            print(f"Submitting in {lang}...")
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
        print("Submission completed.")
        print(__separate_line)


def change_problem(languages, problem_folder):
    input_problem_id = input_until_valid(
        __user_input_problem_id, __allow_all_not_empty, "Problem ID cannot be empty."
    )
    problem_id = back_question_id(input_problem_id)
    for lang in languages:
        cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
        if not cls:
            print(f"{lang} not support.")
            continue
        obj: lc_libs.LanguageWriter = cls()
        obj.change_test(root_path, problem_folder, problem_id)
        print(f"Successfully change {lang} test to {problem_id}")
    print(__separate_line)


def contest_main(languages, contest_folder, cookie):
    def contest_list():
        cur_page = 1
        while True:
            contest_page = contest_lib.get_contest_list(cur_page)
            total, data, has_more = contest_page["total"], contest_page["contests"], contest_page["has_more"]
            max_page = math.ceil(total / 10)
            if not data:
                print("No contests found.")
                break
            contest_content = "\n".join(
                f"{_i}. [{datetime.datetime.fromtimestamp(c['start_time']).strftime('%Y-%m-%d %H:%M:%S')}]{c['title']}"
                for _i, c in enumerate(data, start=1))
            user_input_select = input_until_valid(
                __user_input_page.format(total, contest_content),
                __allow_all
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
            print(__separate_line)
            if not pick:
                continue
            return data[pick - 1]
        return None

    user_input_contest = input_until_valid(
        __user_input_contest,
        __allow_all
    )
    print(__separate_line)
    match user_input_contest:
        case "1":
            contest = contest_list()
            if not contest:
                return None
            contest_id = contest["title_slug"]
        case "2":
            contest_id = input_until_valid(
                __user_input_contest_id,
                __allow_all_not_empty,
                "Contest ID cannot be empty."
            )
        case _:
            return None

    contest_questions = contest_lib.get_contest_info(contest_id)
    p = root_path / contest_folder / contest_id
    p.mkdir(parents=True, exist_ok=True)
    for i, question in enumerate(contest_questions, start=1):
        question_slug = question["title_slug"]
        subp = p / chr(ord('a') + i - 1)
        subp.mkdir(parents=True, exist_ok=True)
        problem_info = contest_lib.get_contest_problem_info(contest_id, question_slug, ["python3"], cookie)
        if not problem_info:
            print(f"Failed to get contest [{contest_id}] problem [{question_slug}]")
            return None
        with (subp / "problem.md").open("w", encoding="utf-8") as f:
            f.write(problem_info["en_markdown_content"])
        with (subp / "problem_zh.md").open("w", encoding="utf-8") as f:
            f.write(problem_info["cn_markdown_content"])
        with (subp / "input.json").open("w", encoding="utf-8") as f:
            json.dump(problem_info["question_example_testcases"], f)
        with (subp / "output.json").open("w", encoding="utf-8") as f:
            json.dump(problem_info["question_example_testcases_output"], f)
        for lang, code in problem_info["language_default_code"].items():
            cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
            if not cls:
                logging.warning(f"Unsupported language {lang} yet")
                continue
            obj: lc_libs.LanguageWriter = cls()
            solution_file = obj.solution_file
            with (subp / solution_file).open("w", encoding="utf-8") as f:
                content = obj.write_contest(code, problem_info["question_id"], "")
                if not content:
                    logging.warning(f"Failed to write solution for {lang}")
                    continue
                f.write(content)
    print(f"Contest [{contest_id}] generated.")
    print(__separate_line)
    return None


def main():
    try:
        languages, problem_folder, cookie, contest_folder = configure()
        while True:
            main_function = input_until_valid(
                __user_input_function,
                __allow_all
            )
            print(__separate_line)
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
                    print("Done cleaning empty Java files.")
                    print(__separate_line)
                case "6":
                    clean_error_rust_main(root_path, problem_folder)
                    print("Done cleaning error Rust files.")
                    print(__separate_line)
                case _:
                    print("Exiting...")
                    break
    except KeyboardInterrupt:
        print("\nBye!")


if __name__ == '__main__':
    main()
    sys.exit()
