import json
import time
import traceback
from collections import defaultdict

import requests


def check_submission(user_slug: str, question_frontend_ids: set[str],
                     min_timestamp=(now := time.time() - time.timezone) - now % 86400 + time.timezone,
                     max_timestamp=None):
    ans = dict()
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"operationName": "recentSubmissions", "variables": {"userSlug": user_slug},
                                     "query": "query recentSubmissions($userSlug: String!) {\n  "
                                              "recentSubmitted(userSlug: $userSlug) {\n    status\n    lang\n    source"
                                              " {\n      sourceType\n      ... on SubmissionSrcLeetbookNode {\n        "
                                              "slug\n        title\n        pageId\n        __typename\n      }\n      "
                                              "__typename\n    }\n    question {\n      questionFrontendId\n      "
                                              "title\n      translatedTitle\n      titleSlug\n      __typename\n    }\n"
                                              "    submitTime\n    __typename\n  }\n}\n"})
        result_dict = json.loads(result.text)['data']['recentSubmitted']
        if result_dict:
            for submit in result_dict:
                if submit['status'] == "A_10" and submit['question']['questionFrontendId'] in question_frontend_ids:
                    t = submit['submitTime']
                    if t >= min_timestamp and (not max_timestamp or t < max_timestamp):
                        ans[submit['question']['questionFrontendId']] = t
                if submit['submitTime'] < min_timestamp:
                    break
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def check_accepted_submission(user_slug: str, min_timestamp=None, max_timestamp=None):
    if min_timestamp is None:
        min_timestamp = (cur_time := time.time() - time.timezone) - cur_time % 86400 + time.timezone
    ans = defaultdict(list)
    try:
        result = requests.post('https://leetcode.cn/graphql/noj-go/',
                               json={"query": "\n    query recentAcSubmissions($userSlug: String!) {\n  "
                                              "recentACSubmissions(userSlug: $userSlug) {\n    submissionId\n    "
                                              "submitTime\n    question {\n      title\n      translatedTitle\n      "
                                              "titleSlug\n      questionFrontendId\n    }\n  }\n}\n    ",
                                     "variables": {"userSlug": user_slug},
                                     "operationName": "recentAcSubmissions"})
        result_dict = json.loads(result.text)['data']['recentACSubmissions']
        if result_dict:
            for submit in result_dict:
                t = submit['submitTime']
                if t < min_timestamp:
                    break
                print(submit)
                if not max_timestamp or t < max_timestamp:
                    ans[submit['question']['questionFrontendId']].append((submit["submissionId"],
                                                                          submit['question']["titleSlug"]))
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def check_accepted_submission_all(user_slug: str, question_frontend_ids):
    ans = dict()
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"operationName": "userProfileQuestions",
                                     "variables": {"status": "ACCEPTED", "skip": 0, "first": 20,
                                                   "sortField": "LAST_SUBMITTED_AT", "sortOrder": "DESCENDING",
                                                   "difficulty": []},
                                     "query": "query userProfileQuestions($status: StatusFilterEnum!, $skip: Int!, "
                                              "$first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!,"
                                              " $keyword: String, $difficulty: [DifficultyEnum!]) {\n  "
                                              "userProfileQuestions(status: $status, skip: $skip, first: $first, "
                                              "sortField: $sortField, sortOrder: $sortOrder, keyword: $keyword, "
                                              "difficulty: $difficulty) {\n    totalNum\n    questions {\n      "
                                              "translatedTitle\n      frontendId\n      titleSlug\n      title\n      "
                                              "difficulty\n      lastSubmittedAt\n      numSubmitted\n      "
                                              "lastSubmissionSrc {\n        sourceType\n        "
                                              "... on SubmissionSrcLeetbookNode {\n          slug\n          title\n   "
                                              "       pageId\n          __typename\n        }\n        __typename\n    "
                                              "  }\n      __typename\n    }\n    __typename\n  }\n}\n"}
                               )
        # TODO:
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def get_submission_detail(submit_id: str, cookie: str):
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"operationName": "mySubmissionDetail",
                                     "variables": {"id": submit_id},
                                     "query": "query mySubmissionDetail($id: ID!) {\n  "
                                              "submissionDetail(submissionId: $id) {\n    id\n    code\n    runtime\n  "
                                              "  memory\n    rawMemory\n    statusDisplay\n    timestamp\n    lang\n   "
                                              " isMine\n    passedTestCaseCnt\n    totalTestCaseCnt\n    sourceUrl\n   "
                                              " question {\n      titleSlug\n      title\n      translatedTitle\n      "
                                              "questionId\n      __typename\n    }\n    ... on GeneralSubmissionNode {\n"
                                              "      outputDetail {\n        codeOutput\n        expectedOutput\n      "
                                              "  input\n        compileError\n        runtimeError\n        "
                                              "lastTestcase\n        __typename\n      }\n      __typename\n    }\n    "
                                              "submissionComment {\n      comment\n      flagType\n      __typename\n  "
                                              "  }\n    __typename\n  }\n}\n"},
                               cookies={"cookie": cookie})
        if result.text:
            result_dict = json.loads(result.text)["data"]["submissionDetail"]
            print(result.text, result_dict)
            return {
                "code": result_dict["code"],
                "lang": result_dict["lang"],
                "runtime": result_dict["runtime"],
                "rawMemory": result_dict["rawMemory"],
                "timestamp": result_dict["timestamp"],
            }
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None
