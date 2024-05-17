import json
import traceback
import requests
from typing import Optional, Dict
from query import DAILY_QUERY


def get_daily_question() -> Optional[Dict]:
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": DAILY_QUERY,
                                     "variables": {}})
        res_dict = json.loads(result.text)
        daily_question = res_dict['data']['todayRecord'][0]
        return {
            'date': daily_question['date'],
            'questionId': daily_question['question']['frontendQuestionId'],
            'questionNameEn': daily_question['question']['title'],
            'questionName': daily_question['question']['titleCn'],
            'questionSlug': daily_question['question']['titleSlug']
        }
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None
