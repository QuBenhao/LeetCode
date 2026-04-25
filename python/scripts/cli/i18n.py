"""
Internationalization (i18n) support for LeetCode CLI
Supports Chinese (zh) and English (en) languages.
"""

import contextvars
from typing import Dict, Any

# Current language setting using ContextVar for thread/coroutine safety
_LANG = contextvars.ContextVar('lang', default='zh')

# Internationalization strings
I18N: Dict[str, Dict[str, str]] = {
    "zh": {
        # Separator
        "sep": "-" * 50,

        # Initialization wizard
        "init_title": "🚀 LeetCode 环境初始化向导",
        "init_step1": "[1/4] 检测浏览器 Cookie...",
        "init_found_cookie": "✓ 从 {browser} 找到 {count} 个 LeetCode Cookies",
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
        "init_cookie_invalid": "⚠️  浏览器中的 Cookie 已过期",
        "init_retry_login": "是否在浏览器中重新登录后重试? [y/n, 默认: y]: ",
        "init_waiting_login": "请在浏览器中登录 leetcode.cn，完成后按回车继续...",
        "init_max_retries": "⚠️  已达最大重试次数，请稍后再试",
        "init_skip_config": "跳过剩余配置步骤，使用现有配置 ({config})? [y/n, 默认: y]: ",
        "init_skip_confirmed": "✓ 使用现有配置",
        "init_load_failed": "⚠️  加载现有配置失败: {error}",

        "init_save_config": "保存配置到 .env 文件? [y/n, 默认: y]: ",
        "init_saved": "✓ 配置已保存到 {path}",
        "init_not_saved": "⚠️  配置未保存，下次启动需重新初始化",
        "init_done": "✅ 初始化完成！",

        # Config selection
        "config_title": "设置环境...",
        "config_select": "请选择配置方式 [0-2, 默认: 0]:\n0. 从 .env 加载默认配置\n1. 自定义配置\n2. 重新初始化 (自动检测浏览器 Cookie)\n",
        "config_auto_detect": "自动检测浏览器 Cookie? [y/n, 默认: y]: ",
        "config_detecting": "正在检测浏览器 Cookie...",
        "config_no_browser_cookie": "浏览器中未找到 Cookie",
        "config_enter_cookie": "输入 LeetCode Cookie (回车使用默认): ",
        "config_cookie_updated": "Cookie 已更新",
        "config_update_env": "更新 .env 文件? [y/n, 默认: n]: ",
        "config_env_updated": "已更新 {path}",

        # Cookie validation
        "cookie_expired": "⚠️  Cookie 可能已过期或无效",
        "cookie_auto_detect": "是否自动从浏览器检测 Cookie? [y/n, 默认: y]: ",
        "cookie_detecting": "🔍 正在检测浏览器 Cookie...",
        "cookie_detected": "✓ 从 {browser} 找到 {count} 个 LeetCode Cookie",
        "cookie_verified": "✓ Cookie 验证成功！",
        "cookie_auto_invalid": "✗ 自动检测的 Cookie 也无效",
        "cookie_auto_expired_hint": "  浏览器中的 Cookie 已过期，请先在浏览器中重新登录 leetcode.cn",
        "cookie_no_browser_hint": "  浏览器中未找到 LeetCode Cookie，请先在浏览器中登录 leetcode.cn",
        "cookie_manual": "是否手动输入 Cookie? [y/n, 默认: n]: ",
        "cookie_continue": "继续使用现有 Cookie...",

        # Main menu
        "main_menu": "请选择功能 [0-9, 默认: 0]:\n0. 退出\n1. 获取题目\n2. 提交代码\n3. 切换测试题目\n4. 比赛\n5. 清理空 Java 文件\n6. 清理错误 Rust 文件\n7. 收藏夹管理\n8. 创建题目链接\n9. 题解中心\n",
        "main_exit": "正在退出...",
        "main_bye": "再见！",

        # Get problem
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

        # Submit
        "submit_menu": "请选择提交方式 [0-4, 默认: 0]:\n0. 返回\n1. 每日提交 [所有语言]\n2. 每日提交 [选择语言]\n3. 指定题目提交 [所有语言]\n4. 指定题目提交 [选择语言]\n",
        "submit_starting": "开始提交，请稍候...",
        "submit_in_lang": "正在提交 {lang}...",
        "submit_done": "提交完成",
        "submit_daily_failed": "无法获取每日题目，可能是网络问题",

        # Contest
        "contest_menu": "请选择比赛方式 [0-2, 默认: 0]:\n0. 返回\n1. 列出比赛\n2. 按 slug 查找\n",
        "contest_type_menu": "请选择比赛类型 [0-2, 默认: 0]:\n0. 返回\n1. 周赛\n2. 双周赛\n",
        "contest_id_num": "输入比赛编号 (如: 1, 2 等): ",
        "contest_id": "输入比赛 ID (如: biweekly-contest-155 等): ",
        "contest_id_empty": "比赛 ID 不能为空",
        "contest_invalid_type": "无效的比赛类型，请重试",
        "contest_no_contests": "未找到比赛",
        "contest_generated": "比赛 [{id}] 已生成",
        "contest_page": "共 [{total}] 项，请选择 [默认: 0]:\n0. 返回\n{content}\n\nb. 上一页\nn. 下一页\n",

        # Favorite
        "fav_menu": "请选择收藏夹操作 [0-2, 默认: 0]:\n0. 返回\n1. 查看收藏夹中的题目\n2. 添加题目到收藏夹\n",
        "fav_no_favorites": "未找到收藏夹",
        "fav_no_questions": "收藏夹中没有题目",
        "fav_add_ids": "输入要添加的题目 ID，用逗号分隔: ",
        "fav_ids_empty": "题目 ID 不能为空",
        "fav_add_success": "成功添加 {count} 道题目到收藏夹 [{name}]",
        "fav_add_failed": "添加题目到收藏夹 [{name}] 失败: {msg}",
        "fav_expired": "Cookie 已过期，请更新后继续",

        # Others
        "tags_not_found": "标签文件未找到，请联系作者",
        "tag_selected": "已选择标签: {tag} [{translations}]",
        "tag_no_problems": "该标签下没有题目",
        "change_test_success": "已将 {lang} 测试切换到 {id}",
        "clean_done": "清理完成",
        "lang_not_support": "{lang} 不支持",

        # Link problems
        "link_target_id": "输入目标题目 ID (创建链接的题目): ",
        "link_source_id": "输入源题目 ID (链接指向的题目): ",
        "link_reason": "输入链接原因 (可选，回车跳过): ",
        "link_delete_solution": "是否删除目标题目的解答文件? [y/n, 默认: n]: ",
        "link_success": "题目 {target} 已链接到 {source}",
        "link_failed": "创建链接失败: {msg}",

        # Fetch solution articles
        "fetch_menu": "请选择拉取方式 [0-3, 默认: 0]:\n0. 返回\n1. 检查所有已解题目 (dry-run)\n2. 拉取所有题解\n3. 拉取指定题目题解\n",
        "fetch_problem_id": "输入题目 ID (回车跳过): ",
        "fetch_force": "是否覆盖已存在的 solution.md? [y/n, 默认: n]: ",
        "fetch_delay": "请求间隔秒数 (回车使用默认 3.0): ",
        "fetch_no_cookie": "未设置 COOKIE，无法拉取题解",
        "fetch_no_user": "未设置 LEETCODE_USER 环境变量",
        "fetch_running": "正在拉取题解...",
        "fetch_done": "拉取完成",

        # Solution center
        "solution_menu": "题解中心 [0-3, 默认: 0]:\n0. 返回\n1. 拉取我的题解\n2. 浏览社区题解\n3. 查看指定作者题解\n",
        "solution_enter_problem_id": "输入题目 ID: ",
        "solution_problem_id_empty": "题目 ID 不能为空",
        "solution_no_articles": "未找到题解",
        "solution_list_header": "社区题解:",
        "solution_select_view": "选择编号查看详情 (0 返回): ",
        "solution_save": "是否保存题解到本地? [y/n, 默认: n]: ",
        "solution_saved": "题解已保存到 {path}",
        "solution_save_failed": "题解保存失败",
        "solution_enter_author": "输入作者 slug (如 endlesscheng, 回车使用默认 endlesscheng): ",
        "solution_author_not_found": "未找到该作者的题解",
        "solution_fetching": "正在获取题解...",
        "solution_loading_detail": "正在加载题解详情...",
        "solution_page": "📖 共 [{total}] 条题解 (第 {page}/{max_page} 页)\n{content}\nb.上一页 | n.下一页 | 编号查看详情 | 回车返回\n",
        "solution_first_page": "已是第一页",
        "solution_last_page": "已是最后一页",
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
        "init_cookie_invalid": "⚠️  Browser cookie has expired",
        "init_retry_login": "Re-login in browser and retry? [y/n, default: y]: ",
        "init_waiting_login": "Please login to leetcode.cn in your browser, then press Enter to continue...",
        "init_max_retries": "⚠️  Max retries reached, please try again later",
        "init_skip_config": "Skip remaining config, use current settings ({config})? [y/n, default: y]: ",
        "init_skip_confirmed": "✓ Using current configuration",
        "init_load_failed": "⚠️  Failed to load existing configuration: {error}",

        "init_save_config": "Save configuration to .env file? [y/n, default: y]: ",
        "init_saved": "✓ Configuration saved to {path}",
        "init_not_saved": "⚠️  Configuration not saved, you'll need to re-initialize next time",
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
        "cookie_auto_expired_hint": "  Browser cookie has expired, please re-login to leetcode.cn in your browser",
        "cookie_no_browser_hint": "  No LeetCode cookie found in browser, please login to leetcode.cn in your browser first",
        "cookie_manual": "Manually enter cookie? [y/n, default: n]: ",
        "cookie_continue": "Continuing with existing cookie...",

        # Main menu
        "main_menu": "Please select the main function [0-9, default: 0]:\n0. Exit\n1. Get problem\n2. Submit\n3. Change test problem\n4. Contest\n5. Clean empty java\n6. Clean error rust\n7. Favorite management\n8. Link problems\n9. Solution Center\n",
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

        # Link problems
        "link_target_id": "Enter target problem ID (the problem to create link for): ",
        "link_source_id": "Enter source problem ID (the problem to link to): ",
        "link_reason": "Enter link reason (optional, press enter to skip): ",
        "link_delete_solution": "Delete solution files in target problem? [y/n, default: n]: ",
        "link_success": "Problem {target} is now linked to {source}",
        "link_failed": "Failed to create link: {msg}",

        # Fetch solution articles
        "fetch_menu": "Please select the fetch method [0-3, default: 0]:\n0. Back\n1. Check all solved problems (dry-run)\n2. Fetch all solution articles\n3. Fetch specified problem solution\n",
        "fetch_problem_id": "Enter problem ID (press enter to skip): ",
        "fetch_force": "Overwrite existing solution.md? [y/n, default: n]: ",
        "fetch_delay": "Request delay in seconds (press enter for default 3.0): ",
        "fetch_no_cookie": "COOKIE not set, unable to fetch solutions",
        "fetch_no_user": "LEETCODE_USER environment variable not set",
        "fetch_running": "Fetching solution articles...",
        "fetch_done": "Fetch completed",

        # Solution center
        "solution_menu": "Solution Center [0-3, default: 0]:\n0. Back\n1. Fetch my solutions\n2. Browse community solutions\n3. View solutions by author\n",
        "solution_enter_problem_id": "Enter problem ID: ",
        "solution_problem_id_empty": "Problem ID cannot be empty",
        "solution_no_articles": "No solutions found",
        "solution_list_header": "Community solutions:",
        "solution_select_view": "Select number to view detail (0 to go back): ",
        "solution_save": "Save solution to local file? [y/n, default: n]: ",
        "solution_saved": "Solution saved to {path}",
        "solution_save_failed": "Failed to save solution",
        "solution_enter_author": "Enter author slug (e.g. endlesscheng, press enter for default endlesscheng): ",
        "solution_author_not_found": "No solution found for this author",
        "solution_fetching": "Fetching solutions...",
        "solution_loading_detail": "Loading solution detail...",
        "solution_page": "📖 Total [{total}] solutions (page {page}/{max_page})\n{content}\nb.Previous | n.Next | Number to view | Enter to go back\n",
        "solution_first_page": "Already on first page",
        "solution_last_page": "Already on last page",
    }
}


def set_language(lang: str) -> None:
    """Set the current language for translations."""
    if lang in I18N:
        _LANG.set(lang)
    else:
        raise ValueError(f"Unsupported language: {lang}. Supported: {list(I18N.keys())}")


def get_language() -> str:
    """Get the current language setting."""
    return _LANG.get()


def t(key: str, **kwargs: Any) -> str:
    """
    Translation function.

    Args:
        key: The translation key
        **kwargs: Format arguments for the translation string

    Returns:
        The translated and formatted string
    """
    lang_dict = I18N.get(_LANG.get(), I18N["zh"])
    text = lang_dict.get(key, I18N["zh"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text
