#!/usr/bin/env python3
"""
全量拉取用户在 LeetCode 发布的题解文章，整理进仓库 articles/ 目录。

用法:
  python python/scripts/fetch_all_my_articles.py [--dry-run] [--limit N] [--force] [--delay S] [--retry-empty] [--status]

说明:
- 列表用 solutionArticles(userSlug) 全量分页拉取（无需登录）
- 正文用 solutionArticle(slug) 拉取（需要登录态 COOKIE，从项目根 .env 读取）
- 输出: articles/<questionTitleSlug>/<slug>.md + articles/_index.json 汇总
- 断点续传: 已存在的 md 文件直接跳过；空正文文章标记 empty，--retry-empty 时补拉
- 健壮性: 每处理一篇就增量写回 _index.json（含 ok/empty/skipped/last_heartbeat），进程被杀也不丢进度
- 启动方式: 用 WorkBuddy 的 run_in_background 启动；会话暂停会断，断后重跑同一条 run 命令即可精确续传
- 判断断没断: 跑 `status` 子命令（查进程存活 + 心跳），或看 /tmp 日志最后修改时间
"""
import argparse
import json
import logging
import os
import random
import subprocess
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / ".env"
ARTICLES_DIR = ROOT / "articles"
GRAPHQL = "https://leetcode.cn/graphql/"
USER_SLUG = "himymben"
PLACEHOLDER = "(内容拉取失败)"

logger = logging.getLogger("fetch_articles")
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


LIST_QUERY = """
query solutionArticles($userSlug: String!, $skip: Int, $first: Int) {
  solutionArticles(userSlug: $userSlug, skip: $skip, first: $first) {
    totalNum
    edges {
      node {
        uuid title slug createdAt status
        tags { name slug tagType }
        summary
        question { questionTitle questionTitleSlug }
        reactionsV2 { count reactionType }
        hitCount
      }
    }
  }
}
"""

CONTENT_QUERY = """
query solutionArticleQuery($slug: String!) {
  solutionArticle(slug: $slug) {
    content title uuid createdAt updatedAt
    tags { name slug }
    upvoteCount
  }
}
"""


def fetch_list(cookie: str, first: int = 20, list_delay: float = 0.3):
    nodes = []
    skip = 0
    total = None
    while True:
        data = _gql(
            LIST_QUERY,
            {"userSlug": USER_SLUG, "skip": skip, "first": first},
            "solutionArticles",
            cookie,
        )
        conn = (data.get("data") or {}).get("solutionArticles") or {}
        if total is None:
            total = conn.get("totalNum", 0)
        edges = conn.get("edges") or []
        for e in edges:
            n = e.get("node")
            if n:
                nodes.append(n)
        if not edges or skip + first >= total:
            break
        skip += first
        time.sleep(list_delay * random.uniform(0.8, 1.3))
    return total, nodes


def fetch_content(slug: str, cookie: str, retries: int = 3):
    for attempt in range(retries):
        try:
            data = _gql(CONTENT_QUERY, {"slug": slug}, "solutionArticleQuery", cookie)
            art = (data.get("data") or {}).get("solutionArticle") or {}
            content = art.get("content")
            if content and content.strip():
                return content
            logger.warning(f"[{slug}] 正文为空 (attempt {attempt + 1})")
        except (HTTPError, URLError) as ex:
            logger.warning(f"[{slug}] 请求失败: {ex} (attempt {attempt + 1})")
        time.sleep(2 * (attempt + 1))
    return None


def is_done(md_path: Path, retry_empty: bool = False) -> bool:
    """已完成 = 文件已存在。

    默认：任何已存在的文件（含占位符）都视为已完成，跳过，避免每轮在
    拉取失败的空文章上重复浪费时间。
    retry_empty=True 时（补拉模式）一律视为未完成，强制重拉。
    """
    if not md_path.exists():
        return False
    if retry_empty:
        return False
    return True


def save_article(node: dict, cookie: str, content_delay: float):
    q = node.get("question") or {}
    qslug = q.get("questionTitleSlug") or "unknown"
    slug = node.get("slug") or node.get("uuid")
    title = node.get("title", "")
    created = (node.get("createdAt") or "")[:10]
    tags = ", ".join(t.get("name", "") for t in node.get("tags", []) if t.get("name"))
    uuid = node.get("uuid", "")
    url = f"https://leetcode.cn/problems/{qslug}/solutions/{uuid}/{slug}/"

    folder = ARTICLES_DIR / qslug
    folder.mkdir(parents=True, exist_ok=True)
    md_path = folder / f"{slug}.md"

    content = fetch_content(slug, cookie)
    head = [
        f"# {title}",
        "",
        f"> slug: {slug}",
        f"> date: {created}",
        f"> tags: {tags}",
        f"> question: {q.get('questionTitle', '')} ({qslug})",
        f"> url: {url}",
        "",
        "---",
        "",
    ]
    md_path.write_text("\n".join(head) + (content or PLACEHOLDER), encoding="utf-8")
    time.sleep(content_delay * random.uniform(0.8, 1.4))
    return "ok" if content else "empty"


def write_index(index_map: dict, total: int):
    items = [index_map[k] for k in sorted(index_map.keys())]
    (ARTICLES_DIR / "_index.json").write_text(
        json.dumps(
            {
                "total": total,
                "fetched": len(items),
                "ok": sum(1 for v in items if v.get("status") == "ok"),
                "empty": sum(1 for v in items if v.get("status") == "empty"),
                "skipped": sum(1 for v in items if v.get("status") == "skipped"),
                "last_heartbeat": time.strftime("%Y-%m-%d %H:%M:%S"),
                "items": items,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def _pgrep_pids(pattern: str, self_pid: int) -> list:
    """返回存活的匹配 pid（排除自身）。无 pgrep 时返回空。"""
    try:
        out = subprocess.run(
            ["pgrep", "-f", pattern], capture_output=True, text=True
        ).stdout
    except Exception:
        return []
    pids = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            p = int(line)
        except ValueError:
            continue
        if p != self_pid:
            pids.append(p)
    return pids


def do_status():
    """打印拉取进度与进程存活状态，不依赖 WorkBuddy 界面。"""
    idx_path = ARTICLES_DIR / "_index.json"
    if not idx_path.exists():
        print("[状态] 尚未开始：没有 _index.json。运行不带 --status 的命令启动拉取。")
        return 0
    try:
        d = json.loads(idx_path.read_text(encoding="utf-8"))
    except Exception as ex:
        print(f"[状态] _index.json 损坏: {ex}")
        return 1
    now = time.time()
    hb = d.get("last_heartbeat")
    if hb:
        try:
            hb_ts = time.mktime(time.strptime(hb, "%Y-%m-%d %H:%M:%S"))
            age = now - hb_ts
        except Exception:
            age = now - idx_path.stat().st_mtime
    else:
        age = now - idx_path.stat().st_mtime
    alive = bool(_pgrep_pids("fetch_all_my_articles.py", os.getpid()))
    total = d.get("total", 0)
    fetched = d.get("fetched", 0)
    ok = d.get("ok", 0)
    empty = d.get("empty", 0)
    skipped = d.get("skipped", 0)
    pct = (fetched / total * 100) if total else 0.0
    if alive:
        state = "✅ 正在运行" if (age is None or age < 120) else "⚠️ 进程在但心跳停滞(可能卡住)"
    else:
        state = "❌ 已停止(会话断开/被杀)，需重启"
    print(f"[状态] {state}")
    print(f"[进度] {fetched}/{total} ({pct:.1f}%)  ok={ok} empty={empty} skipped={skipped}")
    if age is not None:
        print(f"[心跳] 最后活动 {int(age)} 秒前")
    print(f"[重启] python {ROOT / 'python/scripts/fetch_all_my_articles.py'} --delay 1.5")
    return 0


def main():
    ap = argparse.ArgumentParser(description="全量拉取 LeetCode 题解文章")
    ap.add_argument("--dry-run", action="store_true", help="只拉列表不拉正文不写盘")
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 篇（测试用）")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的 md（含占位）")
    ap.add_argument("--retry-empty", action="store_true", help="重拉正文为占位符（拉取失败）的文章")
    ap.add_argument("--delay", type=float, default=1.5, help="正文请求间隔秒数")
    ap.add_argument("--status", action="store_true", help="仅查看进度与进程存活，不拉取")
    args = ap.parse_args()
    if args.status:
        return do_status()

    cookie = load_cookie()
    if not cookie:
        logger.error("未找到 COOKIE（.env 或环境变量），无法拉正文")
        return 1

    logger.info("拉取列表...")
    total, nodes = fetch_list(cookie)
    logger.info(f"列表总数: {total}, 本次取到: {len(nodes)}")
    if args.dry_run:
        for n in nodes[:5]:
            q = n.get("question") or {}
            logger.info(f"  - {n.get('title')} | {q.get('questionTitleSlug')} | {n.get('createdAt','')[:10]}")
        return 0

    if args.limit:
        nodes = nodes[: args.limit]

    index_map = {}
    stats = {"ok": 0, "empty": 0, "skipped": 0}
    for i, n in enumerate(nodes, 1):
        slug = n.get("slug") or n.get("uuid")
        qslug = (n.get("question") or {}).get("questionTitleSlug") or "unknown"
        md_path = ARTICLES_DIR / qslug / f"{slug}.md"

        if not args.force and is_done(md_path, args.retry_empty):
            # 已成功拉取过：记录 skipped，不重复请求
            stats["skipped"] += 1
            index_map[slug] = {
                "title": n.get("title"),
                "slug": slug,
                "uuid": n.get("uuid"),
                "qslug": qslug,
                "question": (n.get("question") or {}).get("questionTitle"),
                "createdAt": n.get("createdAt"),
                "tags": [t.get("name") for t in n.get("tags", []) if t.get("name")],
                "reactions": sum(t.get("count", 0) for t in n.get("reactionsV2", []) if t.get("count")),
                "hitCount": n.get("hitCount"),
                "file": str(md_path.relative_to(ROOT)),
                "status": "skipped",
            }
            # skipped 不频繁写盘，避免刷屏；但仍累计
            continue

        logger.info(f"[{i}/{len(nodes)}] {n.get('title')} ({qslug})")
        res = save_article(n, cookie, args.delay)
        stats[res] = stats.get(res, 0) + 1
        index_map[slug] = {
            "title": n.get("title"),
            "slug": slug,
            "uuid": n.get("uuid"),
            "qslug": qslug,
            "question": (n.get("question") or {}).get("questionTitle"),
            "createdAt": n.get("createdAt"),
            "tags": [t.get("name") for t in n.get("tags", []) if t.get("name")],
            "reactions": sum(t.get("count", 0) for t in n.get("reactionsV2", []) if t.get("count")),
            "hitCount": n.get("hitCount"),
            "file": str(md_path.relative_to(ROOT)),
            "status": res,
        }
        # 每篇增量写盘：进程被杀也不丢进度，且空文章被记录为 empty 便于后续补拉
        write_index(index_map, total)

    write_index(index_map, total)
    logger.info(
        f"完成: ok={stats.get('ok')} empty={stats.get('empty')} "
        f"skipped={stats.get('skipped')} index={ARTICLES_DIR/'_index.json'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
