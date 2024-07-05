import json
from typing import Optional, Dict

from python.constants import LEET_CODE_BACKEND, DAILY_QUERY
from python.utils import general_request, format_question_id


def get_daily_question() -> Optional[Dict]:
    def handle_response(response):
        res_dict = json.loads(response.text)
        daily_question = res_dict['data']['todayRecord'][0]
        return {
            'date': daily_question['date'],
            'questionId': format_question_id(daily_question['question']['frontendQuestionId']),
            'questionNameEn': daily_question['question']['title'],
            'questionName': daily_question['question']['titleCn'],
            'questionSlug': daily_question['question']['titleSlug'],
            "paidOnly": daily_question['question']['paidOnly'],
        }

    return general_request(LEET_CODE_BACKEND, handle_response, json={"query": DAILY_QUERY, "variables": {}})
