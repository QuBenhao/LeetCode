"""
LeetCode 题解文章相关 API
"""

import json
import logging
import re
import time
from typing import Optional, List, Dict

from python.constants.constant import LEET_CODE_BACKEND
from python.constants.solution_article_query import QUESTION_MY_SOLUTION_LIST_QUERY, SOLUTION_ARTICLE_QUERY, QUESTION_SOLUTION_ARTICLES_QUERY
from python.utils.http_tool import general_request


def extract_solution_slug_from_url(url: str) -> Optional[str]:
    """
    从 LeetCode 题解 URL 中提取 slug

    支持的 URL 格式:
    - https://leetcode.cn/problems/{problem}/solutions/{id}/{slug}/
    - https://leetcode.com/problems/{problem}/solutions/{id}/{slug}/
    """
    # 匹配 /solutions/{数字}/{slug}/ 或 /solutions/{数字}/{slug}
    match = re.search(r'/solutions/\d+/([^/?#]+)/?', url)
    if match:
        return match.group(1)
    return None


def get_solution_by_url(url: str, cookie: str) -> Optional[Dict]:
    """
    通过 LeetCode 题解 URL 获取题解内容

    Args:
        url: LeetCode 题解 URL，如 https://leetcode.cn/problems/xxx/solutions/123/slug/
        cookie: LeetCode Cookie

    Returns:
        题解内容字典，包含 title, content, author 等
    """
    slug = extract_solution_slug_from_url(url)
    if not slug:
        logging.warning(f"无法从 URL 提取 slug: {url}")
        return None
    return get_solution_content(slug, cookie)


def get_my_solution_list(question_slug: str, user_slug: str, cookie: str) -> List[Dict]:
    """获取当前用户在指定题目下的题解列表"""
    def handle_response(response):
        data = json.loads(response.text)
        if data.get("errors"):
            logging.warning(f"GraphQL errors in get_my_solution_list: {data['errors']}")
            return []
        if data.get("data") and data["data"].get("questionSolutionMyArticles"):
            return data["data"]["questionSolutionMyArticles"]["edges"]
        return []

    result = general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={
            "query": QUESTION_MY_SOLUTION_LIST_QUERY,
            "variables": {
                "questionSlug": question_slug,
                "skip": 0,
                "first": 20
            },
            "operationName": "questionMySolutionList"
        },
        cookies={'cookie': cookie}
    )

    if not result:
        return []

    # 过滤出当前用户的题解
    filtered = []
    for edge in result:
        node = edge.get("node", {})
        author = node.get("author", {})
        profile = author.get("profile", {})
        author_slug = profile.get("userSlug", "") if profile else ""
        if author_slug.lower() == user_slug.lower():
            filtered.append(node)

    return filtered


def get_solution_content(solution_slug: str, cookie: str, max_retries: int = 3) -> Optional[Dict]:
    """获取题解的详细内容，支持重试"""
    def handle_response(response):
        data = json.loads(response.text)
        if data.get("errors"):
            logging.warning(f"GraphQL errors in get_solution_content: {data['errors']}")
            return None
        if data.get("data") and data["data"].get("solutionArticle"):
            return data["data"]["solutionArticle"]
        return None

    for attempt in range(max_retries):
        result = general_request(
            LEET_CODE_BACKEND,
            handle_response,
            json={
                "query": SOLUTION_ARTICLE_QUERY,
                "variables": {"slug": solution_slug},
                "operationName": "solutionArticleQuery"
            },
            cookies={'cookie': cookie}
        )

        if result:
            # 检查 content 是否为空
            content = result.get("content", "")
            if content and content.strip():
                return result
            else:
                logging.warning(f"Empty content for {solution_slug}, attempt {attempt + 1}/{max_retries}")
                if attempt < max_retries - 1:
                    time.sleep(2 * (attempt + 1))  # 递增等待时间
        else:
            logging.warning(f"Failed to get solution content for {solution_slug}, attempt {attempt + 1}/{max_retries}")
            if attempt < max_retries - 1:
                time.sleep(2 * (attempt + 1))

    return None


def get_solution_articles(question_slug: str, cookie: str, author_slug: str = None,
                          first: int = 15, skip: int = 0, order_by: str = "DEFAULT") -> Dict:
    """
    获取指定题目下的题解列表

    Args:
        question_slug: 题目的 slug，如 'maximize-the-distance-between-points-on-a-square'
        cookie: LeetCode Cookie
        author_slug: 可选，指定作者的 slug，如 'endlesscheng'（使用 userInput 服务端过滤）
        first: 返回数量，默认 15
        skip: 跳过数量，默认 0（用于分页）
        order_by: 排序方式，默认 'DEFAULT'，可选 'MOST_POPULAR'

    Returns:
        字典，包含:
        - total: 总数
        - articles: 题解列表，每个元素包含 slug, title, author, upvoteCount, summary 等
    """
    if not cookie:
        logging.warning("Cookie is empty, cannot fetch solution articles")
        return {"total": 0, "articles": []}

    def handle_response(response):
        data = json.loads(response.text)
        if data.get("errors"):
            logging.warning(f"GraphQL errors in get_solution_articles: {data['errors']}")
            return None
        if data.get("data") and data["data"].get("questionSolutionArticles"):
            result_data = data["data"]["questionSolutionArticles"]
            return {
                "total": result_data.get("totalNum", 0),
                "edges": result_data.get("edges", [])
            }
        return None

    # 当指定 author_slug 时，增大 first 并使用 userInput 服务端过滤
    actual_first = first if not author_slug else min(first * 3, 50)
    user_input = author_slug if author_slug else ""

    result = general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={
            "query": QUESTION_SOLUTION_ARTICLES_QUERY,
            "variables": {
                "questionSlug": question_slug,
                "skip": skip,
                "first": actual_first,
                "orderBy": order_by,
                "userInput": user_input,
                "tagSlugs": []
            },
            "operationName": "questionTopicsList"
        },
        cookies={'cookie': cookie}
    )

    if not result:
        return {"total": 0, "articles": []}

    # 提取 node 数据
    articles = []
    for edge in result.get("edges", []):
        node = edge.get("node", {})
        if author_slug:
            # 服务端已通过 userInput 过滤，客户端再做精确匹配
            author = node.get("author", {})
            profile = author.get("profile", {})
            node_author_slug = profile.get("userSlug", "") if profile else ""
            if node_author_slug.lower() != author_slug.lower():
                continue
        articles.append(node)

    # 当有 author 过滤时，total 使用过滤后的实际数量
    actual_total = len(articles) if author_slug else result.get("total", 0)
    return {"total": actual_total, "articles": articles}


def get_solution_by_author(question_slug: str, author_slug: str, cookie: str) -> Optional[Dict]:
    """
    获取指定作者在指定题目下的题解内容

    Args:
        question_slug: 题目的 slug
        author_slug: 作者的 slug，如 'endlesscheng'
        cookie: LeetCode Cookie

    Returns:
        题解内容字典，包含 title, content, author 等；如果没有找到返回 None
    """
    result = get_solution_articles(question_slug, cookie, author_slug=author_slug)
    articles = result.get("articles", [])
    if not articles:
        return None

    # 取第一个（通常一个作者一个题目只有一篇题解）
    article = articles[0]
    solution_slug = article.get("slug")
    if not solution_slug:
        return None

    return get_solution_content(solution_slug, cookie)
