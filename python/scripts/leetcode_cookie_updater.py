#!/usr/bin/env python3
"""
LeetCode CN Cookie 自动更新工具
从本地浏览器读取 Cookie，自动更新 GitHub Secrets 或本地 .env 文件

使用方法：
1. 安装依赖：pip install browser-cookie3 PyGithub
2. 运行脚本：python leetcode_cookie_updater.py [options]

选项：
  --repo REPO          GitHub 仓库名 (如 QuBenhao/LeetCode)，不指定则不更新 GitHub
  --env PATH           本地 .env 文件路径，不指定则不更新本地文件
  --log-level LEVEL    日志级别: DEBUG, INFO, WARNING, ERROR (默认: INFO)
  --github-token TOKEN GitHub Token (也可通过环境变量 GITHUB_TOKEN 设置)

示例：
  # 只更新 GitHub Secrets
  python leetcode_cookie_updater.py --repo QuBenhao/LeetCode

  # 只更新本地 .env
  python leetcode_cookie_updater.py --env .env

  # 同时更新
  python leetcode_cookie_updater.py --repo QuBenhao/LeetCode --env .env

  # 开启 debug 日志
  python leetcode_cookie_updater.py --repo QuBenhao/LeetCode --log-level DEBUG
"""

import os
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path

# Setup path for importing project modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    import browser_cookie3
except ImportError as e:
    print(f"缺少依赖：{e}")
    print("请运行：pip install browser-cookie3")
    sys.exit(1)

from python.utils import check_cookie_expired


def setup_logging(level: str = "INFO"):
    """设置日志"""
    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=log_format,
        datefmt=date_format,
    )
    return logging.getLogger(__name__)


def get_leetcode_cn_cookie(logger: logging.Logger) -> str | None:
    """从浏览器获取 LeetCode CN 的 Cookie"""
    cookie_parts = []

    # 尝试多种浏览器
    browsers = [
        ('Chrome', browser_cookie3.chrome),
        ('Edge', browser_cookie3.edge),
        ('Firefox', browser_cookie3.firefox),
        ('Chromium', browser_cookie3.chromium),
    ]

    for browser_name, browser_func in browsers:
        try:
            logger.debug(f"尝试从 {browser_name} 获取 cookie...")
            cj = browser_func(domain_name='leetcode.cn')
            cookies = list(cj)
            if cookies:
                logger.info(f"✓ 从 {browser_name} 找到 {len(cookies)} 个 LeetCode CN cookies")
                logger.debug(f"Cookie 名称: {[c.name for c in cookies]}")
                for cookie in cookies:
                    cookie_parts.append(f"{cookie.name}={cookie.value}")
                break
        except Exception as e:
            logger.debug(f"{browser_name} 失败: {type(e).__name__}: {e}")
            continue

    if not cookie_parts:
        logger.error("未在浏览器中找到 LeetCode CN Cookie")
        logger.error("请先在浏览器中访问 leetcode.cn 并登录")
        return None

    cookie = "; ".join(cookie_parts)

    # Check if cookie is expired
    if check_cookie_expired(cookie):
        logger.error("浏览器中的 LeetCode Cookie 已过期")
        logger.error("请先在浏览器中重新登录 leetcode.cn")
        return None

    return cookie


def update_github_secret(cookie: str, repo_name: str, github_token: str, logger: logging.Logger) -> bool:
    """更新 GitHub Secrets"""
    try:
        from github import Github, Auth
    except ImportError:
        logger.error("缺少 PyGithub，请运行：pip install PyGithub")
        return False
    
    logger.debug(f"GitHub Token 长度: {len(github_token)}")
    logger.debug(f"目标仓库: {repo_name}")
    
    try:
        auth = Auth.Token(github_token)
        g = Github(auth=auth)
        
        logger.debug("正在获取仓库信息...")
        repo = g.get_repo(repo_name)
        logger.debug(f"仓库名: {repo.full_name}")
        
        # 检查 token 权限
        user = g.get_user()
        logger.debug(f"当前用户: {user.login}")
        
        # 更新 COOKIE secret
        logger.debug("正在创建/更新 secret COOKIE...")
        repo.create_secret("COOKIE", cookie)
        
        logger.info(f"✓ 已更新 GitHub Secrets: {repo_name}/COOKIE")
        return True
    except Exception as e:
        logger.error(f"更新 GitHub Secrets 失败: {e}")
        
        if "403" in str(e) or "Forbidden" in str(e):
            logger.warning("权限不足！请确保 GitHub Token 有 repo 和 workflow 权限")
        
        logger.debug(f"详细错误: {type(e).__name__}")
        return False


def update_local_env(cookie: str, env_path: str, logger: logging.Logger) -> bool:
    """更新本地 .env 文件"""
    env_file = Path(env_path)
    
    try:
        # 读取现有内容
        lines = []
        cookie_updated = False
        
        if env_file.exists():
            with open(env_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 查找并更新现有的 COOKIE 行
            for i, line in enumerate(lines):
                if line.strip().startswith('COOKIE='):
                    lines[i] = f'COOKIE="{cookie}"\n'
                    cookie_updated = True
                    logger.debug(f"更新现有 COOKIE 行: 第 {i+1} 行")
                    break
        
        # 如果没有找到 COOKIE 行，添加到末尾
        if not cookie_updated:
            if lines and not lines[-1].endswith('\n'):
                lines.append('\n')
            lines.append(f'COOKIE="{cookie}"\n')
            logger.debug("添加新的 COOKIE 行")
        
        # 写回文件
        with open(env_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        logger.info(f"✓ 已更新本地 .env 文件: {env_path}")
        return True
    except Exception as e:
        logger.error(f"更新本地 .env 失败: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="LeetCode CN Cookie 自动更新工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--repo', dest='repo_name', help='GitHub 仓库名 (如 QuBenhao/LeetCode)')
    parser.add_argument('--env', dest='env_path', help='本地 .env 文件路径')
    parser.add_argument('--log-level', dest='log_level', default='INFO',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                        help='日志级别 (默认: INFO)')
    parser.add_argument('--github-token', dest='github_token',
                        help='GitHub Token (也可通过环境变量 GITHUB_TOKEN 设置)')
    
    args = parser.parse_args()
    
    # 设置日志
    logger = setup_logging(args.log_level)
    
    logger.info("=" * 50)
    logger.info("LeetCode CN Cookie 自动更新工具")
    logger.info("=" * 50)
    
    # 检查是否有更新目标
    github_token = args.github_token or os.environ.get('GITHUB_TOKEN')
    update_github = bool(args.repo_name and github_token)
    update_env = bool(args.env_path)
    
    if not update_github and not update_env:
        logger.error("请指定更新目标：")
        logger.error("  --repo REPO_NAME  更新 GitHub Secrets (需要 GITHUB_TOKEN)")
        logger.error("  --env ENV_PATH    更新本地 .env 文件")
        return 1
    
    if args.repo_name and not github_token:
        logger.warning(f"指定了 --repo {args.repo_name} 但未提供 GITHUB_TOKEN，跳过 GitHub 更新")
    
    # 获取 Cookie
    logger.info("[1/2] 从浏览器获取 Cookie...")
    cookie = get_leetcode_cn_cookie(logger)
    
    if not cookie:
        logger.error("获取 Cookie 失败")
        return 1
    
    logger.info(f"✓ Cookie 长度: {len(cookie)} 字符")
    logger.debug(f"Cookie 预览: {cookie[:200]}...")
    
    # 更新目标
    success = True
    step = 0
    total_steps = sum([update_github, update_env])
    
    if update_github:
        step += 1
        logger.info(f"\n[{step}/{total_steps}] 更新 GitHub Secrets...")
        if not update_github_secret(cookie, args.repo_name, github_token, logger):
            success = False
    
    if update_env:
        step += 1
        logger.info(f"\n[{step}/{total_steps}] 更新本地 .env...")
        if not update_local_env(cookie, args.env_path, logger):
            success = False
    
    # 结果
    if success:
        logger.info("\n✅ 完成！")
        return 0
    else:
        logger.error("\n❌ 部分更新失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
