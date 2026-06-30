import json
import logging
from pathlib import Path
from typing import Optional

from python.constants import constant
from python.utils.http_tool import _shared_session


def _update_rating(data_path: Path) -> None:
    response = None
    try:
        response = _shared_session.get(constant.RATING_URL_CN, timeout=5)
    except Exception:
        logging.debug("Timeout for rating data from %s, try to get from %s",
                      constant.RATING_URL_CN, constant.RATING_URL)
    if not response or response.status_code != 200:
        response = _shared_session.get(constant.RATING_URL, timeout=5)
    response.raise_for_status()

    with data_path.open("w", encoding="utf-8") as f:
        f.write(response.text)
    logging.debug("Problems rating data is saved to %s", data_path)


def get_rating(problem_id: str) -> Optional[float]:
    if not problem_id.isnumeric():
        logging.debug("Rating not supporting unique problem."
                      " Current problem id is not numeric: %s", problem_id)
        return None
    try:
        pid = int(problem_id)
        root_path = Path(__file__).parent.parent.parent
        data_path = root_path / "data" / "ratings.json"
        if not data_path.exists():
            _update_rating(data_path)

        def _find_rating() -> Optional[float]:
            with data_path.open("r", encoding="utf-8") as f:
                for problem in json.load(f):
                    if problem["ID"] == pid:
                        return problem["Rating"]
            return None

        result = _find_rating()
        if result is not None:
            return result

        # Rating not found, try refreshing data once
        _update_rating(data_path)
        result = _find_rating()
        if result is not None:
            return result
        logging.debug("Rating not found for problem id: %s", problem_id)
    except Exception as _:
        logging.error("Failed to get rating data.", exc_info=True)
    return None
