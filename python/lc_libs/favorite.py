import logging
from typing import Optional

import requests

from python.constants import LEET_CODE_BACKEND, ADD_QUESTION_TO_FAVORITE_QUERY, MY_FAVORITE_QUERY, \
    FAVORITE_QUESTION_QUERY
from python.utils import general_request


def batch_add_questions_to_favorite(favorite_slug: str, questions: list, cookie: str) -> Optional[dict]:
    def handle_response(response: requests.Response):
        resp = response.json()
        if resp.get("data", {}).get("batchAddQuestionsToFavorite", {}).get("ok"):
            return {"status": "success"}
        else:
            error = resp.get("data", {}).get("batchAddQuestionsToFavorite", {}).get("error", "Unknown error")
            logging.error(f"Failed to add questions to favorite: {error}")
            return {"status": "error", "message": error}

    return general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={"query": ADD_QUESTION_TO_FAVORITE_QUERY,
              "variables": {"favoriteSlug": favorite_slug, "questionSlugs": questions},
              "operationName": "batchAddQuestionsToFavorite"},
        cookies={"cookie": cookie}
    )


def query_my_favorites(cookie: str) -> Optional[dict]:
    def handle_response(response: requests.Response) -> Optional[dict]:
        resp = response.json()

        my_created_favorites = resp.get("data", {}).get("myCreatedFavoriteList", {})
        total_length = my_created_favorites.get("totalLength", 0)
        favorites = my_created_favorites.get("favorites", [])
        return {
            "total": total_length,
            "favorites": [
                {
                    "name": favorite.get("name"),
                    "slug": favorite.get("slug"),
                }
                for favorite in favorites
            ],
            "has_more": my_created_favorites.get("hasMore", False)
        }

    return general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={"query": MY_FAVORITE_QUERY, "operationName": "myFavoriteList", "variables": {}},
        cookies={"cookie": cookie}
    )


def query_favorite_questions(favorite_slug: str, cookie: str, limit: int = 100, skip: int = 0) -> Optional[dict]:
    def handle_response(response: requests.Response) -> Optional[dict]:
        data = response.json().get("data", {}).get("favoriteQuestionList", {})
        total = data.get("totalLength", 0)
        questions = data.get("questions", [])
        return {
            "total": total,
            "questions": [
                {
                    "title": question.get("title"),
                    "title_slug": question.get("titleSlug"),
                    "translated_title": question.get("translatedTitle"),
                    "difficulty": question.get("difficulty"),
                    "id": question.get("id"),
                    "question_frontend_id": question.get("questionFrontendId"),
                }
                for question in questions
            ],
            "has_more": data.get("hasMore", False)
        }

    return general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={
            "query": FAVORITE_QUESTION_QUERY,
            "variables": {
                "skip": skip,
                "limit": limit,
                "favoriteSlug": favorite_slug,
                "filtersV2": {
                    "filterCombineType": "ALL",
                    "statusFilter": {
                        "questionStatuses": [],
                        "operator": "IS"
                    },
                    "difficultyFilter": {
                        "difficulties": [],
                        "operator": "IS"
                    },
                    "languageFilter": {
                        "languageSlugs": [],
                        "operator": "IS"
                    },
                    "topicFilter": {
                        "topicSlugs": [],
                        "operator": "IS"
                    },
                    "acceptanceFilter": {},
                    "frequencyFilter": {},
                    "frontendIdFilter": {},
                    "lastSubmittedFilter": {},
                    "publishedFilter": {},
                    "companyFilter": {
                        "companySlugs": [],
                        "operator": "IS"
                    },
                    "positionFilter": {
                        "positionSlugs": [],
                        "operator": "IS"
                    },
                    "premiumFilter": {
                        "premiumStatus": [],
                        "operator": "IS"
                    }
                },
                "searchKeyword": "",
                "sortBy": {
                    "sortField": "CUSTOM",
                    "sortOrder": "ASCENDING"
                }
            },
            "operationName": "favoriteQuestionList"
        },
        cookies={"cookie": cookie}
    )
