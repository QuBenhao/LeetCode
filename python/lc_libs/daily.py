import json
from typing import Optional, Dict

from constants import LEET_CODE_BACKEND
from query import DAILY_QUERY
from utils import general_request


def get_daily_question() -> Optional[Dict]:
    def handle_response(response):
        res_dict = json.loads(response.text)
        daily_question = res_dict['data']['todayRecord'][0]
        return {
            'date': daily_question['date'],
            'questionId': daily_question['question']['frontendQuestionId'],
            'questionNameEn': daily_question['question']['title'],
            'questionName': daily_question['question']['titleCn'],
            'questionSlug': daily_question['question']['titleSlug']
        }

    return general_request(LEET_CODE_BACKEND, handle_response, json={"query": DAILY_QUERY, "variables": {}})
