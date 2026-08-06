#!/usr/bin/env python3
"""
把 articles/<qslug>/<slug>.md 归位到 problems/problems_<题号>/solution.md。

用法:
  python python/scripts/relocate_articles.py --dry-run    # 只统计，不复制
  python python/scripts/relocate_articles.py              # 实际复制

说明:
- 题号映射来自 solutionArticles(userSlug) 列表接口的 questionFrontendId（需登录态 COOKIE）
- 目标目录: problems/problems_<frontendId 空格转下划线>；LCR/Interview/LCP 等前缀题自然对齐
- 冲突处理: 目标 solution.md 已存在则命名为 solution-<slug前12>.md，绝不覆盖
- 不删除 articles/（保留为全量备份）；只做复制
"""
import argparse
import json
import logging
import os
import shutil
import time
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
ARTICLES_DIR = ROOT / "articles"
PROBLEMS_DIR = ROOT / "problems"
ENV_FILE = ROOT / ".env"
GRAPHQL = "https://leetcode.cn/graphql/"
USER_SLUG = "himymben"

logger = logging.getLogger("relocate")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(_h)


def load_cookie() -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if s.startswith("export "):
                s = s[len("export "):]
            if s.startswith("COOKIE="):
                v = s[len("COOKIE="):].strip()
                return v.strip('"').strip("'")
    return os.getenv("COOKIE", "")


def _gql(query: str, variables: dict, operation: str, cookie: str, timeout: int = 30):
    body = json.dumps(
        {"query": query, "variables": variables, "operationName": operation}
    ).encode("utf-8")
    csrf = ""
    for part in cookie.split(";"):
        part = part.strip()
        if part.startswith("csrftoken="):
            csrf = part[len("csrftoken="):]
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.cn/",
        "User-Agent": "Mozilla/5.0",
        "Cookie": cookie,
    }
    if csrf:
        headers["x-csrftoken"] = csrf
    req = Request(GRAPHQL, data=body, headers=headers)
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


MAPPING_QUERY = """
query solutionArticles($userSlug: String!, $skip: Int, $first: Int) {
  solutionArticles(userSlug: $userSlug, skip: $skip, first: $first) {
    totalNum
    edges {
      node {
        slug
        question { questionTitleSlug questionFrontendId }
      }
    }
  }
}
"""


def fetch_slug_to_id(cookie: str):
    mapping = {}
    skip = 0
    first = 50
    while True:
        data = _gql(
            MAPPING_QUERY,
            {"userSlug": USER_SLUG, "skip": skip, "first": first},
            "solutionArticles",
            cookie,
        )
        conn = (data.get("data") or {}).get("solutionArticles") or {}
        total = conn.get("totalNum", 0)
        edges = conn.get("edges") or []
        for e in edges:
            n = e.get("node") or {}
            slug = n.get("slug")
            q = n.get("question") or {}
            fid = q.get("questionFrontendId")
            if slug and fid:
                mapping[slug] = str(fid).strip()
        if not edges or skip + first >= total:
            break
        skip += first
        time.sleep(0.3)
    return mapping


def target_dir_for(frontend_id: str) -> Path:
    fid = str(frontend_id).strip().replace(" ", "_")
    return PROBLEMS_DIR / f"problems_{fid}"


def relocate(dry_run: bool, only_new: bool = False):
    idx_path = ARTICLES_DIR / "_index.json"
    if not idx_path.exists():
        logger.error("找不到 _index.json，请先跑 fetch_all_my_articles.py")
        return 1
    items = json.loads(idx_path.read_text(encoding="utf-8")).get("items", [])
    cookie = load_cookie()
    if not cookie:
        logger.error("未找到 COOKIE，无法拉题号映射")
        return 1

    logger.info("拉取 slug->题号 映射...")
    mapping = fetch_slug_to_id(cookie)
    logger.info(f"映射数: {len(mapping)}")

    stats = {"moved": 0, "conflict": 0, "nomap": 0, "missing": 0}
    for it in items:
        slug = it.get("slug")
        fpath = ROOT / it.get("file", "")
        if not fpath.exists():
            stats["missing"] += 1
            continue
        fid = mapping.get(slug)
        if not fid:
            stats["nomap"] += 1
            continue
        tdir = target_dir_for(fid)
        tfile = tdir / "solution.md"
        if tfile.exists():
            if only_new:
                stats["conflict"] += 1
                continue
            tfile = tdir / f"solution-{slug[:12]}.md"
            stats["conflict"] += 1
        if dry_run:
            stats["moved"] += 1
            continue
        tdir.mkdir(parents=True, exist_ok=True)
        shutil.copy(str(fpath), str(tfile))
        stats["moved"] += 1

    logger.info(
        f"[dry_run={dry_run}] moved={stats['moved']} conflict={stats['conflict']} "
        f"nomap={stats['nomap']} missing={stats['missing']}"
    )
    return 0


def main():
    ap = argparse.ArgumentParser(description="把题解归位到对应题目目录")
    ap.add_argument("--dry-run", action="store_true", help="只统计不复制")
    ap.add_argument("--only-new", action="store_true", help="只归位无冲突的（目标 solution.md 不存在），跳过已存在的")
    args = ap.parse_args()
    raise SystemExit(relocate(args.dry_run, args.only_new))


if __name__ == "__main__":
    main()
