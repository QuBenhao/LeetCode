import json
import time
import traceback
from collections import defaultdict

import requests

from query import RECENT_SUBMISSIONS_QUERY, RECENT_AC_SUBMISSIONS_QUERY, USER_PROFILE_QUESTIONS_QUERY, \
    PROGRESS_SUBMISSIONS_QUERY, MY_SUBMISSION_DETAIL_QUERY


def check_submission(user_slug: str, question_frontend_ids: set[str],
                     min_timestamp=(now := time.time() - time.timezone) - now % 86400 + time.timezone,
                     max_timestamp=None):
    ans = dict()
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"operationName": "recentSubmissions", "variables": {"userSlug": user_slug},
                                     "query": RECENT_SUBMISSIONS_QUERY})
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
                               json={"query": RECENT_AC_SUBMISSIONS_QUERY,
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
                                                                          submit['question']["titleSlug"], "python3"))
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def check_accepted_submission_all(cookie: str, min_timestamp=None, max_timestamp=None):
    if min_timestamp is None:
        min_timestamp = (cur_time := time.time() - time.timezone) - cur_time % 86400 + time.timezone
    page_no, page_size = 0, 20
    ans = defaultdict(list)
    try:
        query = {"operationName": "userProfileQuestions",
                 "variables": {"status": "ACCEPTED", "skip": page_no * page_size, "first": page_size,
                               "sortField": "LAST_SUBMITTED_AT", "sortOrder": "DESCENDING",
                               "difficulty": []},
                 "query": USER_PROFILE_QUESTIONS_QUERY}
        result = requests.post('https://leetcode.cn/graphql/',
                               json=query,
                               cookies={"cookie": cookie})
        result_dict = json.loads(result.text)['data']['userProfileQuestions']
        if result_dict:
            questions = result_dict['questions']
            while questions and questions[-1]["lastSubmittedAt"] >= min_timestamp and (
                    not max_timestamp or questions[-1]["lastSubmittedAt"] < max_timestamp):
                page_no += 1
                query["variables"]["skip"] = page_no * page_size
                result = requests.post('https://leetcode.cn/graphql/',
                                       json=query,
                                       cookies={"cookie": cookie})
                result_dict = json.loads(result.text)['data']['userProfileQuestions']
                questions.extend(result_dict['questions'])
            while questions and questions[-1]["lastSubmittedAt"] < min_timestamp or (
                    max_timestamp is not None and questions[-1]["lastSubmittedAt"] >= max_timestamp):
                questions.pop()
            for question_submit_info in questions:
                result = requests.post("https://leetcode.cn/graphql/",
                                       json={"operationName": "progressSubmissions",
                                             "variables": {"offset": 0, "limit": 10,
                                                           "questionSlug": question_submit_info["titleSlug"], },
                                             "query": PROGRESS_SUBMISSIONS_QUERY},
                                       cookies={"cookie": cookie})
                result_dict = json.loads(result.text)["data"]["submissionList"]
                for submit in result_dict["submissions"]:
                    t = int(submit['timestamp'])
                    if t < min_timestamp:
                        break
                    print(submit)
                    if not max_timestamp or t < max_timestamp:
                        ans[question_submit_info["frontendId"]].append(
                            (submit["id"], question_submit_info["titleSlug"], submit["lang"]))
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def get_submission_detail(submit_id: str, cookie: str):
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"operationName": "mySubmissionDetail",
                                     "variables": {"id": submit_id},
                                     "query": MY_SUBMISSION_DETAIL_QUERY},
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
