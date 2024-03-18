import json
import traceback

import requests


def get_daily_question() -> dict | None:
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": "\n    query questionOfToday {\n  todayRecord {\n    "
                                              "date\n    userStatus\n    question {\n      "
                                              "questionId\n      frontendQuestionId: "
                                              "questionFrontendId\n      difficulty\n      title\n  "
                                              "    titleCn: translatedTitle\n      titleSlug\n      "
                                              "paidOnly: isPaidOnly\n      freqBar\n      isFavor\n "
                                              "     acRate\n      status\n      solutionNum\n      "
                                              "hasVideoSolution\n      topicTags {\n        name\n  "
                                              "      nameTranslated: translatedName\n        id\n   "
                                              "   }\n      extra {\n        topCompanyTags {\n      "
                                              "    imgUrl\n          slug\n          "
                                              "numSubscribed\n        }\n      }\n    }\n    "
                                              "lastSubmission {\n      id\n    }\n  }\n}\n    ",
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
