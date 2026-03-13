#!/usr/bin/env python3
"""
LeetCode CN Cookie 自动更新工具
从本地浏览器读取 Cookie，自动更新 GitHub Secrets

使用方法:
1. 安装依赖: pip install browser-cookie3 PyGithub
2. 设置环境变量 GITHUB_TOKEN (需要有 repo 权限)
3. 运行脚本: python leetcode_cookie_updater.py

注意: 此脚本需要在有浏览器的本地电脑上运行，不能在服务器上运行
"""

import os
import sys
from datetime import datetime

try:
    import browser_cookie3
    from github import Github
except ImportError as e:
    print(f"缺少依赖: {e}")
    print("请运行: pip install browser-cookie3 PyGithub")
    sys.exit(1)


def get_leetcode_cn_cookie():
    """从浏览器获取 LeetCode CN 的 Cookie"""
    cookie_parts = []
    
    # 尝试多种浏览器
    browsers = [
        ('Chrome', browser_cookie3.chrome),
        ('Edge', browser_cookie3.edge),
        ('Firefox', browser_cookie3.firefox),
    ]
    
    for browser_name, browser_func in browsers:
        try:
            cookies = list(browser_func(domain_name='leetcode.cn'))
            if cookies:
                print(f"✓ 从 {browser_name} 找到 {len(cookies)} 个 LeetCode CN cookies")
                for cookie in cookies:
                    if cookie.value:
                        cookie_parts.append(f"{cookie.name}={cookie.value}")
                break
        except Exception as e:
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
    
    try:
        g = Github(github_token)
        repo = g.get_repo(repo_name)
        
        # 创建或更新 secret
        repo.create_secret("COOKIE", cookie)
        print(f"✓ 已更新 GitHub Secrets: {repo_name}/COOKIE")
        print(f"  时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    except Exception as e:
        print(f"❌ 更新 GitHub Secrets 失败: {e}")
        return False


def main():
    print("=" * 50)
    print("LeetCode CN Cookie 自动更新工具")
    print("=" * 50)
    
    # 检查 GitHub Token
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("❌ 请设置 GITHUB_TOKEN 环境变量")
        print("   export GITHUB_TOKEN='your_token'")
        print("   创建 Token: https://github.com/settings/tokens/new?scopes=repo")
        sys.exit(1)
    
    # 获取 Cookie
    print("\n[1/2] 从浏览器获取 Cookie...")
    cookie = get_leetcode_cn_cookie()
    
    if not cookie:
        print("\n❌ 获取 Cookie 失败")
        print("请确保在浏览器中已登录 leetcode.cn")
        sys.exit(1)
    
    print(f"\n✓ Cookie 长度: {len(cookie)} 字符")
    print(f"  获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 更新 GitHub Secrets
    print("\n[2/2] 更新 GitHub Secrets...")
    if update_github_secret(cookie):
        print("\n" + "=" * 50)
        print("✅ Cookie 更新成功!")
        print("=" * 50)
        print("\n你的 GitHub Actions 现在可以使用新的 Cookie 了")
    else:
        print("\n❌ 更新失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
