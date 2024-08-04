import json
import logging
import os.path
from typing import Optional
import requests

from python.constants import constant


def _update_rating(data_path: str) -> None:
    response = None
    try:
        response = requests.get(constant.RATING_URL_CN, timeout=10)
    except requests.exceptions.Timeout:
        logging.debug("Timeout for rating data from %s, try to get from %s",
                      constant.RATING_URL_CN, constant.RATING_URL)
    if not response or response.status_code != 200:
        response = requests.get(constant.RATING_URL, timeout=30)
    response.raise_for_status()

    with open(data_path, "w") as f:
        f.write(response.text)
    logging.debug("Problems rating data is saved to %s", data_path)


def get_rating(problem_id: str) -> Optional[float]:
    if not problem_id.isnumeric():
        logging.debug("Rating not supporting unique problem."
                      " Current problem id is not numeric: %s", problem_id)
        return None
    try:
        pid = int(problem_id)
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_path = os.path.join(root_path, "data", "ratings.json")
        if not os.path.exists(data_path):
            _update_rating(data_path)
        exist_greater = False
        with open(data_path, "r") as f:
            data = json.load(f)
            for problem in data:
                if problem["ID"] == pid:
                    return problem["Rating"]
                elif problem["ID"] > pid:
                    exist_greater = True
        if not exist_greater:
            logging.debug("Rating not found for problem id: %s", problem_id)
            _update_rating(data_path)
        with open(data_path, "r") as f:
            data = json.load(f)
            for problem in data:
                if problem["ID"] == pid:
                    logging.debug("Rating found for problem id: %s, [%s]", problem_id, problem)
                    return problem["Rating"]
        logging.debug("Rating not found for problem id: %s", problem_id)
    except Exception as _:
        logging.error("Failed to get rating data.", exc_info=True)
    return None
