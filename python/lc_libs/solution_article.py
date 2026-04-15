"""
LeetCode 题解文章相关 API
"""

import json
from typing import Optional, List, Dict

from python.constants.constant import LEET_CODE_BACKEND
from python.constants.solution_article_query import QUESTION_MY_SOLUTION_LIST_QUERY, SOLUTION_ARTICLE_QUERY
from python.utils.http_tool import general_request


def get_my_solution_list(question_slug: str, user_slug: str, cookie: str) -> List[Dict]:
    """获取当前用户在指定题目下的题解列表"""
    def handle_response(response):
        data = json.loads(response.text)
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


def get_solution_content(solution_slug: str, cookie: str) -> Optional[Dict]:
    """获取题解的详细内容"""
    def handle_response(response):
        data = json.loads(response.text)
        if data.get("data") and data["data"].get("solutionArticle"):
            return data["data"]["solutionArticle"]
        return None

    return general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={
            "query": SOLUTION_ARTICLE_QUERY,
            "variables": {"slug": solution_slug},
            "operationName": "solutionArticleQuery"
        },
        cookies={'cookie': cookie}
    )
