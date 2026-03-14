#!/usr/bin/env python3
"""
LeetCode CN Cookie 自动更新工具
从本地浏览器读取 Cookie，自动更新 GitHub Secrets

使用方法：
1. 安装依赖：pip install browser-cookie3 PyGithub
2. 设置环境变量 GITHUB_TOKEN（需要有 repo 权限）
3. 运行脚本：python leetcode_cookie_updater.py

注意：此脚本需要在有浏览器的机器上运行
"""

import os
import sys
from datetime import datetime

# 开启 debug 模式
DEBUG = os.environ.get('DEBUG', '').lower() in ('1', 'true', 'yes')

def debug_log(msg):
    """Debug 日志"""
    if DEBUG:
        print(f"[DEBUG] {msg}")

try:
    import browser_cookie3
    from github import Github
    from github import Auth
except ImportError as e:
    print(f"缺少依赖：{e}")
    print("请运行：pip install browser-cookie3 PyGithub")
    sys.exit(1)


def get_leetcode_cn_cookie():
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
            debug_log(f"尝试从 {browser_name} 获取 cookie...")
            # 尝试获取 leetcode.cn 的 cookie
            cj = browser_func(domain_name='leetcode.cn')
            cookies = list(cj)
            if cookies:
                print(f"✓ 从 {browser_name} 找到 {len(cookies)} 个 LeetCode CN cookies")
                debug_log(f"Cookie 名称: {[c.name for c in cookies]}")
                for cookie in cookies:
                    cookie_parts.append(f"{cookie.name}={cookie.value}")
                break
        except Exception as e:
            debug_log(f"{browser_name} 失败: {type(e).__name__}: {e}")
            print(f"✗ {browser_name}: {e}")
            continue
    
    if not cookie_parts:
        print("❌ 未找到 LeetCode CN Cookie")
        print("请确保你已经在浏览器中登录过 leetcode.cn")
        return None
    
    return "; ".join(cookie_parts)


def update_github_secret(cookie: str, repo_name: str = "QuBenhao/LeetCode"):
    """更新 GitHub Secrets"""
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("❌ 请设置 GITHUB_TOKEN 环境变量")
        return False
    
    debug_log(f"GitHub Token 长度: {len(github_token)}")
    debug_log(f"GitHub Token 前缀: {github_token[:10]}...")
    debug_log(f"目标仓库: {repo_name}")
    
    try:
        # 使用新的 API 格式
        auth = Auth.Token(github_token)
        g = Github(auth=auth)
        
        debug_log("正在获取仓库信息...")
        repo = g.get_repo(repo_name)
        debug_log(f"仓库名: {repo.full_name}")
        
        # 检查 token 权限
        user = g.get_user()
        debug_log(f"当前用户: {user.login}")
        
        # 更新 COOKIE secret
        debug_log("正在创建/更新 secret COOKIE...")
        repo.create_secret("COOKIE", cookie)
        
        print(f"✓ 已更新 GitHub Secrets: {repo_name}/COOKIE")
        print(f"  时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    except Exception as e:
        print(f"❌ 更新 GitHub Secrets 失败: {e}")
        
        # 检查是否是权限问题
        if "403" in str(e) or "Forbidden" in str(e):
            print("\n⚠️  权限不足！请确保你的 GitHub Token 有以下权限：")
            print("  - repo (完整仓库访问)")
            print("  - workflow (更新 GitHub Actions)")
            print("\n创建新 Token 的步骤：")
            print("  1. 访问 https://github.com/settings/tokens")
            print("  2. 点击 'Generate new token (classic)'")
            print("  3. 勾选 'repo' 和 'workflow' 权限")
            print("  4. 生成并保存 Token")
        
        debug_log(f"详细错误: {type(e).__name__}")
        return False


def main():
    print("=" * 50)
    print("LeetCode CN Cookie 自动更新工具")
    print("=" * 50)
    
    if DEBUG:
        print("[DEBUG 模式已开启]")
    
    # 获取 Cookie
    print("\n[1/2] 从浏览器获取 Cookie...")
    cookie = get_leetcode_cn_cookie()
    
    if not cookie:
        print("\n❌ 获取 Cookie 失败")
        return 1
    
    print(f"\n✓ Cookie 长度: {len(cookie)} 字符")
    print(f" 获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if DEBUG:
        print(f"[DEBUG] Cookie 预览: {cookie[:200]}...")
    
    # 更新 GitHub Secrets
    print("\n[2/2] 更新 GitHub Secrets...")
    if update_github_secret(cookie):
        print("\n✅ 完成！Cookie 已自动更新")
        print("  你的 GitHub Actions 现在可以使用新的 Cookie 了")
        return 0
    else:
        print("\n❌ 更新失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
