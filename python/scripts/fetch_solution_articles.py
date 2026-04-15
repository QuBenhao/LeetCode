#!/usr/bin/env python3
"""
LeetCode 题解拉取工具
从 LeetCode 拉取用户发布的题解，保存到本地 problem 目录

使用方法:
  PYTHONPATH=. python python/scripts/fetch_solution_articles.py [--dry-run] [--force] [--problem-id ID]

环境变量:
  USER: LeetCode 用户名 (slug)
  PROBLEM_FOLDER: 题目文件夹名 (默认 problems)
  COOKIE: LeetCode Cookie (获取题解内容需要)
"""

import argparse
import logging
import os
import re
import random
import sys
import time
from pathlib import Path
from typing import Optional, List, Dict

from dotenv import load_dotenv

# Setup paths
file_path = Path(__file__)
root_path = file_path.parent.parent.parent
sys.path.insert(0, str(root_path))

from python.utils.str_util import back_question_id, format_question_id
from python.lc_libs.question import get_questions_by_key_word
from python.lc_libs.solution_article import get_my_solution_list, get_solution_content


def get_question_slug_by_id(problem_id: str, cookie: str) -> Optional[Dict]:
    """根据题目ID获取题目的slug和标题"""
    questions = get_questions_by_key_word(problem_id, cookie)
    if not questions:
        return None

    formatted_id = format_question_id(problem_id)
    for question in questions:
        if question.get("questionFrontendId") == formatted_id:
            return {
                "titleSlug": question.get("titleSlug"),
                "title": question.get("title"),
            }
    return None


def generate_solution_md(solution_data: Dict, question_info: Dict) -> str:
    """生成 solution.md 文件内容"""
    title = solution_data.get("title", "")
    content = solution_data.get("content", "")
    author = solution_data.get("author", {})
    profile = author.get("profile", {})
    tags = solution_data.get("tags", [])
    upvote_count = solution_data.get("upvoteCount", 0)
    created_at = solution_data.get("createdAt", "")

    # 获取作者名称
    author_name = profile.get("realName", "") if profile else ""
    if not author_name:
        author_name = profile.get("userSlug", "") if profile else ""
    if not author_name:
        author_name = author.get("username", "Unknown")

    # 解析 tags
    tag_names = [t.get("name", "") for t in tags if t.get("name")]

    # 格式化日期
    if created_at:
        try:
            from datetime import datetime
            dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            date_str = dt.strftime("%Y-%m-%d")
        except Exception:
            date_str = created_at[:10] if len(created_at) >= 10 else created_at
    else:
        date_str = ""

    # 构建 markdown
    md_parts = [
        f"# {title}",
        "",
        f"> Author: {author_name}",
        f"> Date: {date_str}",
        f"> Upvotes: {upvote_count}",
    ]
    if tag_names:
        md_parts.append(f"> Tags: {', '.join(tag_names)}")

    md_parts.extend([
        "",
        "---",
        "",
        content
    ])

    return "\n".join(md_parts)


def get_solved_problems(problem_folder: str) -> List[str]:
    """获取已解决问题的ID列表"""
    problems_path = root_path / problem_folder
    if not problems_path.exists():
        return []

    solved_ids = []
    pattern = re.compile(rf"^{problem_folder}_(\d+)$")

    for item in problems_path.iterdir():
        if item.is_dir():
            match = pattern.match(item.name)
            if match:
                problem_dir = item
                # 检查是否有解法文件
                has_solution = any(
                    (problem_dir / f).exists()
                    for f in ["solution.py", "solution.go", "Solution.java",
                              "Solution.cpp", "solution.rs", "solution.ts"]
                )
                if has_solution:
                    solved_ids.append(match.group(1))

    return sorted(solved_ids, key=lambda x: int(x) if x.isdigit() else float('inf'))


def main(dry_run: bool = False, force: bool = False, problem_id: Optional[str] = None,
         delay: float = 1.0, verbose: bool = False,
         user_slug: Optional[str] = None, problem_folder: Optional[str] = None,
         cookie: Optional[str] = None):
    """
    主函数，可被其他模块调用

    Args:
        dry_run: 只检查不保存
        force: 强制覆盖已存在的 solution.md
        problem_id: 指定题目ID
        delay: 请求间隔秒数
        verbose: 详细输出
        user_slug: 用户名 (可选，从环境变量读取)
        problem_folder: 题目文件夹 (可选，从环境变量读取)
        cookie: LeetCode Cookie (可选，从环境变量读取)
    """
    # 设置日志
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format="[%(levelname)s] %(message)s")

    # 加载环境变量 (override=True 以覆盖已存在的系统环境变量)
    load_dotenv(root_path / ".env", override=True)

    # 从参数或环境变量获取配置
    user_slug = user_slug or os.getenv("USER", "")
    if not user_slug:
        logging.error("未设置 USER 环境变量")
        return 1

    problem_folder = problem_folder or os.getenv("PROBLEM_FOLDER", "problems")
    cookie = cookie or os.getenv("COOKIE", "")

    if not cookie:
        logging.error("未设置 COOKIE 环境变量，获取题解需要登录态")
        return 1

    logging.info(f"用户: {user_slug}")
    logging.info(f"题目目录: {problem_folder}")
    logging.info(f"Dry run: {dry_run}")
    logging.info(f"请求间隔: {delay}s")

    # 获取要处理的题目
    if problem_id:
        problem_ids = [back_question_id(problem_id)]
    else:
        problem_ids = get_solved_problems(problem_folder)

    if not problem_ids:
        logging.warning("没有找到已解决的题目")
        return 0

    logging.info(f"发现 {len(problem_ids)} 道已解决题目")

    # 统计
    stats = {
        "total": len(problem_ids),
        "checked": 0,
        "has_solution": 0,
        "downloaded": 0,
        "skipped": 0,
        "error": 0
    }

    for i, pid in enumerate(problem_ids, 1):
        stats["checked"] += 1
        problem_dir = root_path / problem_folder / f"{problem_folder}_{pid}"
        solution_file = problem_dir / "solution.md"

        logging.debug(f"[{i}/{len(problem_ids)}] 处理题目 {pid}")

        # 检查是否已存在
        if solution_file.exists() and not force:
            logging.debug(f"[{pid}] 已存在 solution.md，跳过")
            stats["skipped"] += 1
            continue

        # 获取题目 slug
        question_info = get_question_slug_by_id(pid, cookie)

        if not question_info:
            logging.warning(f"[{pid}] 无法获取题目信息")
            stats["error"] += 1
            continue

        question_slug = question_info.get("titleSlug", "")
        question_title = question_info.get("title", "")

        # 获取用户题解列表
        my_solutions = get_my_solution_list(question_slug, user_slug, cookie)

        if not my_solutions:
            logging.debug(f"[{pid}] {question_title}: 没有发布题解")
            continue

        stats["has_solution"] += 1

        # 选择最新的题解 (按 createdAt 排序)
        latest_solution = max(my_solutions, key=lambda x: x.get("createdAt", ""))

        if dry_run:
            logging.info(f"[{pid}] {question_title}: 发现题解 '{latest_solution.get('title')}' (dry-run)")
            stats["downloaded"] += 1
            continue

        # 获取题解详细内容
        sol_slug = latest_solution.get("slug", "")
        solution_content = get_solution_content(sol_slug, cookie)

        if not solution_content:
            logging.warning(f"[{pid}] 无法获取题解内容: {sol_slug}")
            stats["error"] += 1
            continue

        # 生成并保存 solution.md
        md_content = generate_solution_md(solution_content, question_info)
        problem_dir.mkdir(parents=True, exist_ok=True)

        with open(solution_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        logging.info(f"[{pid}] {question_title}: 已保存题解 '{solution_content.get('title')}'")
        stats["downloaded"] += 1

        # 避免请求过快，增加随机抖动
        jitter = random.uniform(0, 0.3)
        time.sleep(delay + jitter)

    # 打印统计
    logging.info("=" * 50)
    logging.info("统计:")
    logging.info(f"  检查题目: {stats['checked']}")
    logging.info(f"  发现题解: {stats['has_solution']}")
    logging.info(f"  {'已保存' if not dry_run else '将保存'}: {stats['downloaded']}")
    logging.info(f"  跳过(已存在): {stats['skipped']}")
    logging.info(f"  错误: {stats['error']}")

    return 0


def cli_main():
    """命令行入口"""
    parser = argparse.ArgumentParser(description="LeetCode 题解拉取工具")
    parser.add_argument("--dry-run", action="store_true", help="只检查不保存")
    parser.add_argument("--force", action="store_true", help="强制覆盖已存在的 solution.md")
    parser.add_argument("--problem-id", type=str, help="指定题目ID (可选)")
    parser.add_argument("--delay", type=float, default=1.0, help="请求间隔秒数 (默认1.0)")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()

    return main(
        dry_run=args.dry_run,
        force=args.force,
        problem_id=args.problem_id,
        delay=args.delay,
        verbose=args.verbose
    )


if __name__ == "__main__":
    sys.exit(cli_main())
