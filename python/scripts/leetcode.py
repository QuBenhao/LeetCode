import asyncio
import json
import logging
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
from python.lc_libs import get_daily_question
from python.scripts.submit import main as submit_main_async
from python.utils import back_question_id, format_question_id
from python.scripts.daily_auto import main as daily_auto_main
from python.scripts.get_problem import main as get_problem_main
from python.scripts.tools import lucky_main, remain_main, clean_empty_java_main, clean_error_rust_main

__separate_line = "-" * 50

__user_input_config = """Please select the configuration [0-1, default: 0]:
0. Load default config from .env
1. Custom config
"""
__user_input_function = """Please select the main function [0-4, default: 0]:
0. Exit
1. Get problem
2. Submit
3. Clean empty java
4. Clean error rust
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
__user_input_problem_id = "Enter the problem ID (e.g., 1, LCR 043, 面试题 01.01, etc.): "

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

        input_cookie = input_until_valid(
            "Enter your LeetCode cookie (press enter to use default): ",
            __allow_all
        )
        if input_cookie:
            cookie = input_cookie.strip()
        else:
            cookie = os.getenv(constant.COOKIE)
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
        cookie = os.getenv(constant.COOKIE)
        problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        languages = os.getenv(constant.LANGUAGES, "python3").split(",")
        print(f"Languages selected: {', '.join(languages)}")
        print(f"Problem folder selected: {problem_folder}")
        print(__separate_line)

    logging.basicConfig(level=logging.ERROR)
    return languages, problem_folder, cookie


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


def main():
    try:
        languages, problem_folder, cookie = configure()
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
                    clean_empty_java_main(root_path, problem_folder)
                    print("Done cleaning empty Java files.")
                    print(__separate_line)
                case "4":
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
