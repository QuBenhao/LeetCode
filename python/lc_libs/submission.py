import json
import time
from collections import defaultdict

import requests

from python.constants import (LEET_CODE_BACKEND, RECENT_SUBMISSIONS_QUERY, RECENT_AC_SUBMISSIONS_QUERY,
                       USER_PROFILE_QUESTIONS_QUERY, PROGRESS_SUBMISSIONS_QUERY, MY_SUBMISSION_DETAIL_QUERY)
from python.utils import general_request


def check_submission(user_slug: str, question_frontend_ids: set[str],
                     min_timestamp=(now := time.time() - time.timezone) - now % 86400 + time.timezone,
                     max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['recentSubmitted']
        if result_dict:
            for submit in result_dict:
                if submit['status'] == "A_10" and submit['question']['questionFrontendId'] in question_frontend_ids:
                    t = submit['submitTime']
                    if t >= min_timestamp and (not max_timestamp or t < max_timestamp):
                        ans[submit['question']['questionFrontendId']] = t
                if submit['submitTime'] < min_timestamp:
                    break

    ans = dict()
    general_request(LEET_CODE_BACKEND,
                    handle_response,
                    json={"operationName": "recentSubmissions", "variables": {"userSlug": user_slug},
                          "query": RECENT_SUBMISSIONS_QUERY})

    return ans


def check_accepted_submission(user_slug: str, min_timestamp=None, max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['recentACSubmissions']
        if result_dict:
            for submit in result_dict:
                t = submit['submitTime']
                if t < min_timestamp:
                    break
                print(submit)
                if not max_timestamp or t < max_timestamp:
                    ans[submit['question']['questionFrontendId']].append((submit["submissionId"],
                                                                          submit['question']["titleSlug"], "python3"))

    if min_timestamp is None:
        min_timestamp = (cur_time := time.time() - time.timezone) - cur_time % 86400 + time.timezone
    ans = defaultdict(list)
    general_request('https://leetcode.cn/graphql/noj-go/', handle_response,
                    json={"query": RECENT_AC_SUBMISSIONS_QUERY,
                          "variables": {"userSlug": user_slug},
                          "operationName": "recentAcSubmissions"})
    return ans


def check_accepted_submission_all(cookie: str, min_timestamp=None, max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['userProfileQuestions']
        return result_dict['questions'] if result_dict else []

    def handle_response_submissions(response: requests.Response):
        result_dict = json.loads(response.text)["data"]["submissionList"]
        for submit in result_dict["submissions"]:
            t = int(submit['timestamp'])
            if t < min_timestamp:
                break
            print(submit)
            if not max_timestamp or t < max_timestamp:
                ans[question_submit_info["frontendId"]].append(
                    (submit["id"], question_submit_info["titleSlug"], submit["lang"]))

    if min_timestamp is None:
        min_timestamp = (cur_time := time.time() - time.timezone) - cur_time % 86400 + time.timezone
    page_no, page_size = 0, 20
    ans = defaultdict(list)
    query = {"operationName": "userProfileQuestions",
             "variables": {"status": "ACCEPTED", "skip": page_no * page_size, "first": page_size,
                           "sortField": "LAST_SUBMITTED_AT", "sortOrder": "DESCENDING",
                           "difficulty": []},
             "query": USER_PROFILE_QUESTIONS_QUERY}
    questions = general_request(LEET_CODE_BACKEND, handle_response,
                                json=query,
                                cookies={"cookie": cookie})
    if not questions:
        return ans
    while questions and questions[-1]["lastSubmittedAt"] >= min_timestamp and (
            not max_timestamp or questions[-1]["lastSubmittedAt"] < max_timestamp):
        page_no += 1
        query["variables"]["skip"] = page_no * page_size
        questions.extend(general_request(LEET_CODE_BACKEND, handle_response,
                                         json=query,
                                         cookies={"cookie": cookie}))
    while questions and questions[-1]["lastSubmittedAt"] < min_timestamp or (
            max_timestamp is not None and questions[-1]["lastSubmittedAt"] >= max_timestamp):
        questions.pop()
    for question_submit_info in questions:
        general_request("https://leetcode.cn/graphql/", handle_response_submissions,
                        json={"operationName": "progressSubmissions",
                              "variables": {"offset": 0, "limit": 10,
                                            "questionSlug": question_submit_info["titleSlug"], },
                              "query": PROGRESS_SUBMISSIONS_QUERY},
                        cookies={"cookie": cookie})

    return ans


def get_submission_detail(submit_id: str, cookie: str):
    def handle_response(response: requests.Response):
        if not response.text:
            return None
        result_dict = json.loads(response.text)["data"]["submissionDetail"]
        return {
            "code": result_dict["code"],
            "lang": result_dict["lang"],
            "runtime": result_dict["runtimeDisplay"],
            "rawMemory": result_dict["memory"],
            "timestamp": result_dict["timestamp"],
        }

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={"operationName": "submissionDetails",
                                 "variables": {"submissionId": submit_id},
                                 "query": MY_SUBMISSION_DETAIL_QUERY},
                           cookies={"cookie": cookie})
