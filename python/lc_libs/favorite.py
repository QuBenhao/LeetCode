import logging
from typing import Optional

import requests

from python.constants import LEET_CODE_BACKEND, ADD_QUESTION_TO_FAVORITE_QUERY, MY_FAVORITE_QUERY
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
    def handle_response(response: requests.Response) -> Optional[list]:
        resp = response.json()
        my_created_favorites = resp.get("data", {}).get("myCreatedFavoriteList", {}).get("favorites", [])
        return [
            {
                "name": favorite.get("name"),
                "slug": favorite.get("slug"),
            }
            for favorite in my_created_favorites
        ]

    return general_request(
        LEET_CODE_BACKEND,
        handle_response,
        json={"query": MY_FAVORITE_QUERY, "operationName": "myFavoriteList", "variables": {}},
        cookies={"cookie": cookie}
    )
