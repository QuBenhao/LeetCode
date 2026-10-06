"""
APIs for LeetCode solution articles
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
    Extract the slug from a LeetCode solution URL

    Supported URL formats:
    - https://leetcode.cn/problems/{problem}/solutions/{id}/{slug}/
    - https://leetcode.com/problems/{problem}/solutions/{id}/{slug}/
    """
    # Match /solutions/{number}/{slug}/ or /solutions/{number}/{slug}
    match = re.search(r'/solutions/\d+/([^/?#]+)/?', url)
    if match:
        return match.group(1)
    return None


def get_solution_by_url(url: str, cookie: str) -> Optional[Dict]:
    """
    Fetch solution content through a LeetCode solution URL

    Args:
        url: LeetCode solution URL, such as https://leetcode.cn/problems/xxx/solutions/123/slug/
        cookie: LeetCode Cookie

    Returns:
        Dictionary of solution content, including title, content, author, etc.
    """
    slug = extract_solution_slug_from_url(url)
    if not slug:
        logging.warning(f"无法从 URL 提取 slug: {url}")
        return None
    return get_solution_content(slug, cookie)


def get_my_solution_list(question_slug: str, user_slug: str, cookie: str) -> List[Dict]:
    """Get the current user's solutions for the specified problem."""
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

    # Filter for the current user's solutions
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
    """Get detailed solution content, with retry support."""
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
            # Check whether content is empty
            content = result.get("content", "")
            if content and content.strip():
                return result
            else:
                logging.warning(f"Empty content for {solution_slug}, attempt {attempt + 1}/{max_retries}")
                if attempt < max_retries - 1:
                    time.sleep(2 * (attempt + 1))  # Increase the wait time
        else:
            logging.warning(f"Failed to get solution content for {solution_slug}, attempt {attempt + 1}/{max_retries}")
            if attempt < max_retries - 1:
                time.sleep(2 * (attempt + 1))

    return None


def get_solution_articles(question_slug: str, cookie: str, author_slug: str = None,
                          first: int = 15, skip: int = 0, order_by: str = "DEFAULT") -> Dict:
    """
    Get solutions for the specified problem

    Args:
        question_slug: Problem slug, such as 'maximize-the-distance-between-points-on-a-square'
        cookie: LeetCode Cookie
        author_slug: Optional author slug, such as 'endlesscheng' (uses server-side userInput filtering)
        first: Number of results to return; defaults to 15
        skip: Number of results to skip; defaults to 0 (for pagination)
        order_by: Sort order; defaults to 'DEFAULT', with 'MOST_POPULAR' also supported

    Returns:
        Dictionary containing:
        - total: Total count
        - articles: List of solutions, each containing slug, title, author, upvoteCount, summary, etc.
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

    # When author_slug is provided, increase first and use server-side userInput filtering
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

    # Extract node data
    articles = []
    for edge in result.get("edges", []):
        node = edge.get("node", {})
        if author_slug:
            # The server filters by userInput; also require an exact match on the client
            author = node.get("author", {})
            profile = author.get("profile", {})
            node_author_slug = profile.get("userSlug", "") if profile else ""
            if node_author_slug.lower() != author_slug.lower():
                continue
        articles.append(node)

    # With an author filter, use the actual filtered count for total
    actual_total = len(articles) if author_slug else result.get("total", 0)
    return {"total": actual_total, "articles": articles}


def get_solution_by_author(question_slug: str, author_slug: str, cookie: str) -> Optional[Dict]:
    """
    Get a specified author's solution content for the specified problem

    Args:
        question_slug: Problem slug
        author_slug: Author slug, such as 'endlesscheng'
        cookie: LeetCode Cookie

    Returns:
        Dictionary of solution content, including title, content, author, etc.; None if not found
    """
    result = get_solution_articles(question_slug, cookie, author_slug=author_slug)
    articles = result.get("articles", [])
    if not articles:
        return None

    # Take the first result (an author usually has only one solution per problem)
    article = articles[0]
    solution_slug = article.get("slug")
    if not solution_slug:
        return None

    return get_solution_content(solution_slug, cookie)
