#!/usr/bin/env python3
"""
LeetCode 工具集 - 主入口
支持交互式初始化、浏览器 Cookie 自动检测、多语言界面

使用方法：
  python leetcode.py           # 默认中文界面
  python leetcode.py --en      # 英文界面
  python leetcode.py --init    # 强制进入初始化向导
"""

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
import argparse
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path
from dotenv import load_dotenv

file_path = Path(__file__)
root_path = file_path.parent.parent.parent
sys.path.insert(0, root_path.as_posix())

from python.constants import constant
from python.lc_libs import get_daily_question, query_my_favorites, batch_add_questions_to_favorite, \
    query_favorite_questions, contest as contest_lib
import python.lc_libs as lc_libs
from python.scripts.submit import main as submit_main_async
from python.utils import back_question_id, format_question_id, check_cookie_expired
from python.scripts.daily_auto import main as daily_auto_main
from python.scripts.get_problem import main as get_problem_main, get_question_slug_by_id
from python.scripts.tools import lucky_main, remain_main, clean_empty_java_main, clean_error_rust_main

# Optional: browser_cookie3 for auto-detecting LeetCode cookie
try:
    import browser_cookie3
    HAS_BROWSER_COOKIE = True
except ImportError:
    HAS_BROWSER_COOKIE = False

# ============================================================================
# 国际化支持 / Internationalization
# ============================================================================

LANG = "zh"  # 默认中文

I18N = {
    "zh": {
        # 分隔线
        "sep": "-" * 50,
        
        # 初始化向导
        "init_title": "🚀 LeetCode 环境初始化向导",
        "init_step1": "[1/4] 检测浏览器 Cookie...",
        "init_found_cookie": "✓ 从 {browser} 找到 {count} 个 LeetCode Cookie",
        "init_no_cookie": "✗ 未在浏览器中找到 LeetCode Cookie",
        "init_no_cookie_hint": "  请确保你已在浏览器中登录 leetcode.cn",
        "init_browser_not_installed": "✗ 未安装 browser_cookie3",
        "init_browser_install_hint": "  安装命令: pip install browser-cookie3",
        "init_enter_cookie": "请手动输入 LeetCode Cookie: ",
        "init_cookie_empty": "Cookie 不能为空",
        
        "init_step2": "[2/4] 选择编程语言",
        "init_select_lang": "选择要使用的编程语言，用逗号分隔 [0-5, 默认: 0]:\n{options}\n",
        "init_lang_selected": "✓ 已选择语言: {langs}",
        "init_lang_invalid": "输入无效，请输入 0-5 的数字，用逗号分隔",
        
        "init_step3": "[3/4] 配置目录",
        "init_problem_folder": "题目目录路径 (回车使用默认 'problems'): ",
        "init_contest_folder": "比赛目录路径 (回车使用默认 'contest'): ",
        "init_folder_selected": "✓ 题目目录: {folder}",
        
        "init_step4": "[4/4] 可选：配置通知",
        "init_push_key": "PushDeer 推送 Key (回车跳过): ",
        "init_notify_configured": "✓ 已配置 PushDeer 通知",
        "init_notify_skipped": "✓ 已跳过通知配置",
        
        "init_verifying": "🔍 验证 Cookie...",
        "init_cookie_valid": "✓ Cookie 验证成功！",
        "init_cookie_invalid": "⚠️  Cookie 无效，可能需要刷新浏览器登录",
        
        "init_save_config": "保存配置到 .env 文件? [y/n, 默认: y]: ",
        "init_saved": "✓ 配置已保存到 {path}",
        "init_done": "✅ 初始化完成！",
        
        # 配置选择
        "config_title": "设置环境...",
        "config_select": "请选择配置方式 [0-2, 默认: 0]:\n0. 从 .env 加载默认配置\n1. 自定义配置\n2. 重新初始化 (自动检测浏览器 Cookie)\n",
        "config_auto_detect": "自动检测浏览器 Cookie? [y/n, 默认: y]: ",
        "config_detecting": "正在检测浏览器 Cookie...",
        "config_no_browser_cookie": "浏览器中未找到 Cookie",
        "config_enter_cookie": "输入 LeetCode Cookie (回车使用默认): ",
        "config_cookie_updated": "Cookie 已更新",
        "config_update_env": "更新 .env 文件? [y/n, 默认: n]: ",
        "config_env_updated": "已更新 {path}",
        
        # Cookie 验证
        "cookie_expired": "⚠️  Cookie 可能已过期或无效",
        "cookie_auto_detect": "是否自动从浏览器检测 Cookie? [y/n, 默认: y]: ",
        "cookie_detecting": "🔍 正在检测浏览器 Cookie...",
        "cookie_detected": "✓ 从 {browser} 找到 {count} 个 LeetCode Cookie",
        "cookie_verified": "✓ Cookie 验证成功！",
        "cookie_auto_invalid": "✗ 自动检测的 Cookie 也无效",
        "cookie_manual": "是否手动输入 Cookie? [y/n, 默认: n]: ",
        "cookie_continue": "继续使用现有 Cookie...",
        
        # 主菜单
        "main_menu": "请选择功能 [0-7, 默认: 0]:\n0. 退出\n1. 获取题目\n2. 提交代码\n3. 切换测试题目\n4. 比赛\n5. 清理空 Java 文件\n6. 清理错误 Rust 文件\n7. 收藏夹管理\n",
        "main_exit": "正在退出...",
        "main_bye": "再见！",
        
        # 获取题目
        "get_menu": "请选择获取题目方式 [0-6, 默认: 0]:\n0. 返回\n1. 每日自动\n2. 指定题目 ID\n3. 随机\n4. 随机未通过\n5. 分类\n6. 比赛\n",
        "get_problem_id": "输入题目 ID (如: 1, LCR 043, 面试题 01.01 等): ",
        "get_problem_id_empty": "题目 ID 不能为空",
        "get_success": "题目 [{id}] 获取成功",
        "get_failed": "获取题目失败，请检查题目 ID: {id}",
        "get_daily_success": "每日自动获取完成",
        "get_daily_failed": "每日自动获取失败",
        "get_random_success": "随机题目获取成功",
        "get_random_failed": "随机题目获取失败，请重试",
        "get_remain_failed": "获取随机未通过题目失败，Cookie 可能无效或没有未通过的题目",
        
        # 提交
        "submit_menu": "请选择提交方式 [0-4, 默认: 0]:\n0. 返回\n1. 每日提交 [所有语言]\n2. 每日提交 [选择语言]\n3. 指定题目提交 [所有语言]\n4. 指定题目提交 [选择语言]\n",
        "submit_starting": "开始提交，请稍候...",
        "submit_in_lang": "正在提交 {lang}...",
        "submit_done": "提交完成",
        "submit_daily_failed": "无法获取每日题目，可能是网络问题",
        
        # 比赛
        "contest_menu": "请选择比赛方式 [0-2, 默认: 0]:\n0. 返回\n1. 列出比赛\n2. 按 slug 查找\n",
        "contest_type_menu": "请选择比赛类型 [0-2, 默认: 0]:\n0. 返回\n1. 周赛\n2. 双周赛\n",
        "contest_id_num": "输入比赛编号 (如: 1, 2 等): ",
        "contest_id": "输入比赛 ID (如: biweekly-contest-155 等): ",
        "contest_id_empty": "比赛 ID 不能为空",
        "contest_invalid_type": "无效的比赛类型，请重试",
        "contest_no_contests": "未找到比赛",
        "contest_generated": "比赛 [{id}] 已生成",
        "contest_page": "共 [{total}] 项，请选择 [默认: 0]:\n0. 返回\n{content}\n\nb. 上一页\nn. 下一页\n",
        
        # 收藏夹
        "fav_menu": "请选择收藏夹操作 [0-2, 默认: 0]:\n0. 返回\n1. 查看收藏夹中的题目\n2. 添加题目到收藏夹\n",
        "fav_no_favorites": "未找到收藏夹",
        "fav_no_questions": "收藏夹中没有题目",
        "fav_add_ids": "输入要添加的题目 ID，用逗号分隔: ",
        "fav_ids_empty": "题目 ID 不能为空",
        "fav_add_success": "成功添加 {count} 道题目到收藏夹 [{name}]",
        "fav_add_failed": "添加题目到收藏夹 [{name}] 失败: {msg}",
        "fav_expired": "Cookie 已过期，请更新后继续",
        
        # 其他
        "tags_not_found": "标签文件未找到，请联系作者",
        "tag_selected": "已选择标签: {tag} [{translations}]",
        "tag_no_problems": "该标签下没有题目",
        "change_test_success": "已将 {lang} 测试切换到 {id}",
        "clean_done": "清理完成",
        "lang_not_support": "{lang} 不支持",
    },
    "en": {
        # Separator
        "sep": "-" * 50,
        
        # Initialization wizard
        "init_title": "🚀 LeetCode Environment Initialization",
        "init_step1": "[1/4] Detecting browser cookie...",
        "init_found_cookie": "✓ Found {count} LeetCode cookies from {browser}",
        "init_no_cookie": "✗ No LeetCode cookie found in browsers",
        "init_no_cookie_hint": "  Please make sure you have logged in to leetcode.cn",
        "init_browser_not_installed": "✗ browser_cookie3 not installed",
        "init_browser_install_hint": "  Install with: pip install browser-cookie3",
        "init_enter_cookie": "Enter LeetCode Cookie manually: ",
        "init_cookie_empty": "Cookie cannot be empty",
        
        "init_step2": "[2/4] Select programming languages",
        "init_select_lang": "Select languages, separated by comma [0-5, default: 0]:\n{options}\n",
        "init_lang_selected": "✓ Languages selected: {langs}",
        "init_lang_invalid": "Invalid input, please enter numbers 0-5 separated by comma",
        
        "init_step3": "[3/4] Configure directories",
        "init_problem_folder": "Problem folder path (press enter for 'problems'): ",
        "init_contest_folder": "Contest folder path (press enter for 'contest'): ",
        "init_folder_selected": "✓ Problem folder: {folder}",
        
        "init_step4": "[4/4] Optional: Configure notifications",
        "init_push_key": "PushDeer key for notifications (press enter to skip): ",
        "init_notify_configured": "✓ PushDeer notification configured",
        "init_notify_skipped": "✓ Skipped notification setup",
        
        "init_verifying": "🔍 Verifying cookie...",
        "init_cookie_valid": "✓ Cookie verified successfully!",
        "init_cookie_invalid": "⚠️  Cookie is invalid, you may need to refresh browser login",
        
        "init_save_config": "Save configuration to .env file? [y/n, default: y]: ",
        "init_saved": "✓ Configuration saved to {path}",
        "init_done": "✅ Initialization complete!",
        
        # Config selection
        "config_title": "Setting up the environment...",
        "config_select": "Please select the configuration [0-2, default: 0]:\n0. Load default config from .env\n1. Custom config\n2. Re-initialize (auto-detect browser cookie)\n",
        "config_auto_detect": "Auto-detect cookie from browser? [y/n, default: y]: ",
        "config_detecting": "Detecting browser cookie...",
        "config_no_browser_cookie": "No cookie found in browsers",
        "config_enter_cookie": "Enter your LeetCode cookie (press enter to use default): ",
        "config_cookie_updated": "Cookie updated",
        "config_update_env": "Update .env file? [y/n, default: n]: ",
        "config_env_updated": "Updated {path}",
        
        # Cookie validation
        "cookie_expired": "⚠️  Cookie might be expired or invalid",
        "cookie_auto_detect": "Auto-detect cookie from browser? [y/n, default: y]: ",
        "cookie_detecting": "🔍 Detecting browser cookie...",
        "cookie_detected": "✓ Found {count} LeetCode cookies from {browser}",
        "cookie_verified": "✓ Cookie verified successfully!",
        "cookie_auto_invalid": "✗ Auto-detected cookie is also invalid",
        "cookie_manual": "Manually enter cookie? [y/n, default: n]: ",
        "cookie_continue": "Continuing with existing cookie...",
        
        # Main menu
        "main_menu": "Please select the main function [0-7, default: 0]:\n0. Exit\n1. Get problem\n2. Submit\n3. Change test problem\n4. Contest\n5. Clean empty java\n6. Clean error rust\n7. Favorite management\n",
        "main_exit": "Exiting...",
        "main_bye": "Bye!",
        
        # Get problem
        "get_menu": "Please select the get problem method [0-6, default: 0]:\n0. Back\n1. Daily auto\n2. Specified problem ID\n3. Random\n4. Random remain\n5. Category\n6. Contest\n",
        "get_problem_id": "Enter the problem ID (e.g. 1, LCR 043, 面试题 01.01, etc.): ",
        "get_problem_id_empty": "Problem ID cannot be empty",
        "get_success": "Problem [{id}] fetched successfully",
        "get_failed": "Failed to fetch the problem. Make sure the problem ID is correct: {id}",
        "get_daily_success": "Daily auto completed successfully",
        "get_daily_failed": "Daily auto failed",
        "get_random_success": "Random problem fetched successfully",
        "get_random_failed": "Failed to fetch a random problem. Please try again",
        "get_remain_failed": "Failed to fetch random remaining problem. Cookie may be invalid or no remaining problems",
        
        # Submit
        "submit_menu": "Please select the submit method [0-4, default: 0]:\n0. Back\n1. Daily submit[All selected languages]\n2. Daily submit[Select language]\n3. Submit specified problem[All selected languages]\n4. Submit specified problem[Select language]\n",
        "submit_starting": "Starting submission, please wait...",
        "submit_in_lang": "Submitting in {lang}...",
        "submit_done": "Submission completed",
        "submit_daily_failed": "Unable to get daily question, possibly network issue",
        
        # Contest
        "contest_menu": "Please select the contest method [0-2, default: 0]:\n0. Back\n1. List contests\n2. Contest by slug\n",
        "contest_type_menu": "Please select the contest type [0-2, default: 0]:\n0. Back\n1. Weekly contest\n2. Biweekly contest\n",
        "contest_id_num": "Enter the contest ID number (e.g. 1, 2, etc.): ",
        "contest_id": "Enter the contest ID (e.g. biweekly-contest-155, etc.): ",
        "contest_id_empty": "Contest ID cannot be empty",
        "contest_invalid_type": "Invalid contest type, please try again",
        "contest_no_contests": "No contests found",
        "contest_generated": "Contest [{id}] generated",
        "contest_page": "Total of [{total}] elements, please select [default: 0]:\n0. Back\n{content}\n\nb. last page\nn. next page\n",
        
        # Favorite
        "fav_menu": "Please select the favorite method [0-2, default: 0]:\n0. Back\n1. List problems in the favorite\n2. Add problems to the favorite\n",
        "fav_no_favorites": "No favorites found",
        "fav_no_questions": "No questions found in this favorite",
        "fav_add_ids": "Enter the problem ids to add to favorite, separated by comma: ",
        "fav_ids_empty": "Problem ids cannot be empty",
        "fav_add_success": "Added {count} questions to favorite [{name}] successfully",
        "fav_add_failed": "Failed to add questions to favorite [{name}]: {msg}",
        "fav_expired": "Cookie expired, please update it to continue",
        
        # Others
        "tags_not_found": "Tags file not found. Please contact the author",
        "tag_selected": "Selected tag: {tag} [{translations}]",
        "tag_no_problems": "No problems found for this tag",
        "change_test_success": "Successfully change {lang} test to {id}",
        "clean_done": "Done",
        "lang_not_support": "{lang} not support",
    }
}

def t(key, **kwargs):
    """翻译函数 / Translation function"""
    text = I18N.get(LANG, I18N["zh"]).get(key, I18N["zh"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text

__separate_line = "-" * 50

__supported_languages = ["python3", "java", "golang", "cpp", "typescript", "rust"]

__allow_all = lambda x: True
__allow_all_not_empty = lambda x: bool(x.strip())
__allow_number = lambda x: bool(re.match(r"^\d+$", x))


def input_until_valid(prompt, check_func, error_msg=None):
    while True:
        try:
            user_input = input(prompt)
            if check_func(user_input):
                return user_input
            elif error_msg:
                print(error_msg)
            print(__separate_line)
        except EOFError:
            # 处理管道输入结束
            sys.exit(0)


def input_pick_array(desc, arr):
    user_input = input_until_valid(
        f"Enter the number of the {desc} [1-{len(arr)}, or 0 to go back (default), or input random to random:\n"
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


def get_browser_cookie():
    """Auto-detect LeetCode CN cookie from browser"""
    if not HAS_BROWSER_COOKIE:
        return None
    
    browsers = [
        ('Chrome', browser_cookie3.chrome),
        ('Edge', browser_cookie3.edge),
        ('Firefox', browser_cookie3.firefox),
        ('Chromium', browser_cookie3.chromium),
    ]
    
    for browser_name, browser_func in browsers:
        try:
            cj = browser_func(domain_name='leetcode.cn')
            cookies = list(cj)
            if cookies:
                cookie_parts = [f"{c.name}={c.value}" for c in cookies]
                return "; ".join(cookie_parts), browser_name, len(cookies)
        except Exception:
            continue
    
    return None


def read_cookie_from_file():
    """从文件读取 Cookie (解决终端输入长度限制)"""
    # 尝试从临时文件读取
    cookie_file = root_path / ".cookie_tmp"
    if cookie_file.exists():
        try:
            cookie = cookie_file.read_text(encoding='utf-8').strip()
            if cookie:
                print(f"✓ 从 .cookie_tmp 读取到 Cookie")
                # 读取后删除临时文件
                cookie_file.unlink()
                return cookie
        except Exception:
            pass
    
    # 提示用户可以从文件输入
    print("\n💡 提示: Cookie 较长时，可以保存到 .cookie_tmp 文件，脚本会自动读取")
    print("   或者使用管道输入: cat cookie.txt | python leetcode.py")
    return None


def check_and_update_cookie(_cookie: str, auto_detect: bool = True) -> str:
    """Check cookie validity and prompt for update if needed"""
    while check_cookie_expired(_cookie):
        print(t("cookie_expired"))
        
        # Try auto-detect from browser
        if auto_detect and HAS_BROWSER_COOKIE:
            auto_detect_choice = input_until_valid(
                t("cookie_auto_detect"),
                __allow_all
            )
            if auto_detect_choice != "n":
                print(t("cookie_detecting"))
                result = get_browser_cookie()
                if result:
                    cookie, browser_name, cookie_count = result
                    print(t("cookie_detected", browser=browser_name, count=cookie_count))
                    # Verify the new cookie
                    if not check_cookie_expired(cookie):
                        print(t("cookie_verified"))
                        return cookie
                    else:
                        print(t("cookie_auto_invalid"))
                        print(t("init_no_cookie_hint"))
                else:
                    print(t("init_no_cookie"))
                    print(t("init_no_cookie_hint"))
        
        # Try reading from file
        file_cookie = read_cookie_from_file()
        if file_cookie and not check_cookie_expired(file_cookie):
            print(t("cookie_verified"))
            return file_cookie
        
        # Manual input
        update_cookie = input_until_valid(
            t("cookie_manual"),
            __allow_all
        )
        if update_cookie == "y":
            print("\n💡 Cookie 较长时，建议保存到 .cookie_tmp 文件后重试")
            _cookie = input_until_valid(
                t("init_enter_cookie"),
                __allow_all_not_empty,
                t("init_cookie_empty")
            )
            print(t("config_cookie_updated"))
        else:
            print(t("cookie_continue"))
            break
        print(__separate_line)
    return _cookie


def initialize_env():
    """Interactive environment initialization wizard"""
    print("\n" + "=" * 50)
    print(t("init_title"))
    print("=" * 50)
    
    env_file = root_path / ".env"
    
    # Step 1: Auto-detect browser cookie
    print(f"\n{t('init_step1')}")
    cookie = None
    if HAS_BROWSER_COOKIE:
        result = get_browser_cookie()
        if result:
            cookie, browser_name, cookie_count = result
            print(t("init_found_cookie", browser=browser_name, count=cookie_count))
        else:
            print(t("init_no_cookie"))
            print(t("init_no_cookie_hint"))
    else:
        print(t("init_browser_not_installed"))
        print(t("init_browser_install_hint"))
    
    if not cookie:
        # 尝试从文件读取
        cookie = read_cookie_from_file()
        if not cookie:
            cookie = input_until_valid(
                t("init_enter_cookie"),
                __allow_all_not_empty,
                t("init_cookie_empty")
            )
    print(__separate_line)
    
    # Step 2: Select languages
    print(f"\n{t('init_step2')}")
    lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(__supported_languages))
    pick_languages = input_until_valid(
        t("init_select_lang", options=lang_options),
        lambda x: re.match(r"^[0-5](,[0-5])*$", x),
        t("init_lang_invalid")
    )
    languages = list(set(__supported_languages[int(idx)] for idx in pick_languages.split(",")))
    print(t("init_lang_selected", langs=", ".join(languages)))
    print(__separate_line)
    
    # Step 3: Set problem folder
    print(f"\n{t('init_step3')}")
    input_problem_folder = input_until_valid(
        t("init_problem_folder"),
        __allow_all
    )
    problem_folder = input_problem_folder if input_problem_folder else "problems"
    print(t("init_folder_selected", folder=problem_folder))
    
    input_contest_folder = input_until_valid(
        t("init_contest_folder"),
        __allow_all
    )
    contest_folder = input_contest_folder if input_contest_folder else "contest"
    print(t("init_folder_selected", folder=contest_folder))
    print(__separate_line)
    
    # Step 4: Optional notification
    print(f"\n{t('init_step4')}")
    push_key = input_until_valid(
        t("init_push_key"),
        __allow_all
    )
    if push_key:
        print(t("init_notify_configured"))
    else:
        print(t("init_notify_skipped"))
    print(__separate_line)
    
    # Verify cookie
    print(f"\n{t('init_verifying')}")
    if check_cookie_expired(cookie):
        print(t("init_cookie_invalid"))
    else:
        print(t("init_cookie_valid"))
    print(__separate_line)
    
    # Save to .env
    save_config = input_until_valid(
        t("init_save_config"),
        __allow_all
    )
    if save_config != "n":
        with env_file.open("w") as f:
            f.write(f'{constant.COOKIE}="{cookie}"\n')
            f.write(f'{constant.PROBLEM_FOLDER}="{problem_folder}"\n')
            f.write(f'{constant.CONTEST_FOLDER}="{contest_folder}"\n')
            f.write(f'{constant.LANGUAGES}="{",".join(languages)}"\n')
            if push_key:
                f.write(f'{constant.PUSH_KEY}="{push_key}"\n')
            f.write('PYTHONPATH=.\n')
        print(t("init_saved", path=env_file))
    
    print("\n" + "=" * 50)
    print(t("init_done"))
    print("=" * 50 + "\n")
    
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
    config_select = input_until_valid(t("config_select"), __allow_all)
    print(__separate_line)
    
    if config_select == "2":
        # Re-initialize
        return initialize_env()
    
    if config_select == "1":
        # Custom config
        lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(__supported_languages))
        pick_languages = input_until_valid(
            t("init_select_lang", options=lang_options),
            lambda x: re.match(r"^[0-5](,[0-5])*$", x),
            t("init_lang_invalid")
        )
        languages = list(set(__supported_languages[int(idx)] for idx in pick_languages.split(",")))
        print(t("init_lang_selected", langs=", ".join(languages)))
        print(__separate_line)

        input_problem_folder = input_until_valid(
            t("init_problem_folder"),
            __allow_all
        )
        problem_folder = input_problem_folder if input_problem_folder else os.getenv(constant.PROBLEM_FOLDER, "problems")
        print(t("init_folder_selected", folder=problem_folder))
        print(__separate_line)

        input_contest_folder = input_until_valid(
            t("init_contest_folder"),
            __allow_all
        )
        contest_folder = input_contest_folder if input_contest_folder else os.getenv(constant.CONTEST_FOLDER, "contest")
        print(t("init_folder_selected", folder=contest_folder))
        print(__separate_line)

        # Try auto-detect cookie first
        cookie = None
        if HAS_BROWSER_COOKIE:
            auto_detect = input_until_valid(
                t("config_auto_detect"),
                __allow_all
            )
            if auto_detect != "n":
                print(t("config_detecting"))
                result = get_browser_cookie()
                if result:
                    cookie, browser_name, cookie_count = result
                    print(t("init_found_cookie", browser=browser_name, count=cookie_count))
                else:
                    print(t("config_no_browser_cookie"))
                print(__separate_line)
        
        if not cookie:
            # 尝试从文件读取
            cookie = read_cookie_from_file()
            if not cookie:
                input_cookie = input_until_valid(
                    t("config_enter_cookie"),
                    __allow_all
                )
                cookie = input_cookie.strip() if input_cookie else os.getenv(constant.COOKIE)
        
        cookie = check_and_update_cookie(cookie)
        print(__separate_line)

        update_config = input_until_valid(
            t("config_update_env"),
            __allow_all
        )
        if update_config == "y":
            with env_file.open("w") as f:
                f.write(f'{constant.COOKIE}="{cookie}"\n')
                f.write(f'{constant.PROBLEM_FOLDER}="{problem_folder}"\n')
                f.write(f'{constant.CONTEST_FOLDER}="{contest_folder}"\n')
                f.write(f'{constant.LANGUAGES}="{",".join(languages)}"\n')
            print(t("config_env_updated", path=env_file))
        print(__separate_line)
    else:
        # Load from .env
        cookie = check_and_update_cookie(os.getenv(constant.COOKIE))
        problem_folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        contest_folder = os.getenv(constant.CONTEST_FOLDER, "contest")
        languages = os.getenv(constant.LANGUAGES, "python3").split(",")
        print(t("init_lang_selected", langs=", ".join(languages)))
        print(t("init_folder_selected", folder=problem_folder))
        print(t("init_folder_selected", folder=contest_folder))
        print(__separate_line)

    logging.basicConfig(level=logging.ERROR)
    return languages, problem_folder, cookie, contest_folder


def get_problem(languages, problem_folder, cookie):
    while True:
        get_problem_method = input_until_valid(
            t("get_menu"),
            __allow_all
        )
        print(__separate_line)
        match get_problem_method:
            case "1":
                exit_code = daily_auto_main(problem_folder, cookie, languages)
                if exit_code == 0:
                    print(t("get_daily_success"))
                else:
                    print(t("get_daily_failed"))
            case "2":
                input_problem_id = input_until_valid(
                    t("get_problem_id"), __allow_all_not_empty, t("get_problem_id_empty")
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
                tags = root_path / "data" / "tags.json"
                if not tags.exists():
                    print(t("tags_not_found"))
                    continue
                with tags.open("r", encoding="utf-8") as f:
                    json_tags = json.load(f)
                tags = list(json_tags.keys())
                pick_tag = input_pick_array("tag", tags)
                if pick_tag is None:
                    continue
                tag = tags[pick_tag]
                tag_data = json_tags[tag]
                print(t("tag_selected", tag=tag, translations=",".join(tag_data.get('translations', []))))
                print(__separate_line)
                problems = tag_data.get("problems", [])
                if not problems:
                    print(t("tag_no_problems"))
                    continue
                pick_problem = input_pick_array("problem", problems)
                if pick_problem is None:
                    continue
                problem_id = problems[pick_problem]
                exit_code = get_problem_main(
                    problem_id, force=True, cookie=cookie, replace_problem_id=True, skip_language=True,
                    languages=languages, problem_folder=problem_folder
                )
                if exit_code == 0:
                    print(t("get_success", id=problem_id))
                else:
                    print(t("get_failed", id=problem_id))
            case "6":
                contest_type = input_until_valid(
                    t("contest_type_menu"),
                    lambda x: x in ["0", "1", "2"],
                    t("contest_invalid_type")
                )
                print(__separate_line)
                contest_id = input_until_valid(
                    t("contest_id_num"),
                    __allow_number,
                    t("contest_id_empty")
                )
                print(__separate_line)
                if contest_type == "0":
                    return
                elif contest_type == "1":
                    contest_id = f"weekly-contest-{contest_id}"
                elif contest_type == "2":
                    contest_id = f"biweekly-contest-{contest_id}"
                else:
                    print(t("contest_invalid_type"))
                    continue
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
            case _:
                return


def submit(languages, problem_folder, cookie):
    while True:
        submit_method = input_until_valid(
            t("submit_menu"),
            __allow_all
        )
        print(__separate_line)
        if submit_method == "2" or submit_method == "4":
            lang_options = "\n".join(f"{idx}. {lang}" for idx, lang in enumerate(__supported_languages))
            language_select = input_until_valid(
                t("init_select_lang", options=lang_options),
                lambda x: re.match(r"^[0-5](,[0-5])*$", x),
                t("init_lang_invalid")
            )
            languages = list(set(__supported_languages[int(idx)] for idx in language_select.split(",")))
            print(__separate_line)
        match submit_method:
            case "1" | "2":
                daily_info = get_daily_question()
                if not daily_info:
                    print(t("submit_daily_failed"))
                    continue
                problem_id = daily_info['questionId']
            case "3" | "4":
                input_problem_id = input_until_valid(
                    t("get_problem_id"), __allow_all_not_empty, t("get_problem_id_empty")
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
        print(__separate_line)


def change_problem(languages, problem_folder):
    input_problem_id = input_until_valid(
        t("get_problem_id"), __allow_all_not_empty, t("get_problem_id_empty")
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
    print(__separate_line)


def contest_main(languages, contest_folder, cookie):
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
        t("contest_menu"),
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
                t("contest_id"),
                __allow_all_not_empty,
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
    print(__separate_line)
    return None


def favorite_main(languages, problem_folder, cookie):
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
                __allow_all
            )
            pick = None
            match user_input_select:
                case v if v.isdigit() and 1 <= int(v) <= 10:
                    pick = int(v)
                case _:
                    break
            print(__separate_line)
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
                __allow_all
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
            print(__separate_line)
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
                __allow_all
            )
            print(__separate_line)
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
                        __allow_all_not_empty,
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


def main():
    global LANG
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="LeetCode 工具集")
    parser.add_argument('--en', action='store_true', help='Use English interface')
    parser.add_argument('--init', action='store_true', help='Force initialization wizard')
    args = parser.parse_args()
    
    # 设置语言
    if args.en:
        LANG = "en"
    
    try:
        if args.init:
            languages, problem_folder, cookie, contest_folder = initialize_env()
        else:
            languages, problem_folder, cookie, contest_folder = configure()
        
        while True:
            main_function = input_until_valid(
                t("main_menu"),
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
                    print(t("clean_done"))
                    print(__separate_line)
                case "6":
                    clean_error_rust_main(root_path, problem_folder)
                    print(t("clean_done"))
                    print(__separate_line)
                case "7":
                    favorite_main(languages, problem_folder, cookie)
                    print(__separate_line)
                case _:
                    print(t("main_exit"))
                    break
    except KeyboardInterrupt:
        print(f"\n{t('main_bye')}")


if __name__ == '__main__':
    main()
    sys.exit()
