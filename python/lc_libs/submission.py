import json
import random
import time
from collections import defaultdict

import requests
from tqdm import tqdm

from python.constants import (LEET_CODE_BACKEND, RECENT_SUBMISSIONS_QUERY, RECENT_AC_SUBMISSIONS_QUERY,
                              USER_PROFILE_QUESTIONS_QUERY, PROGRESS_SUBMISSIONS_QUERY, MY_SUBMISSION_DETAIL_QUERY,
                              SUBMIT_SUCCESS_RESULT, SUBMIT_BASIC_RESULT, SUBMIT_FAIL_RESULT)
from python.utils import general_request, get_china_daily_time


def check_submission(user_slug: str, question_frontend_ids: set[str],
                     min_timestamp=None,
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

    if min_timestamp is None:
        min_timestamp = get_china_daily_time()
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
        min_timestamp = get_china_daily_time()
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
        min_timestamp = get_china_daily_time()
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


def get_submission_detail(submit_id: str, cookie: str, handle_fun=None):
    def handle_response(response: requests.Response):
        if not response.text:
            return None
        result_dict = json.loads(response.text)["data"]["submissionDetail"]
        if result_dict['statusDisplay'] != 'Accepted':
            # wrong solution, add testcase
            return {
                "statusDisplay": result_dict["statusDisplay"],
                "input": result_dict["outputDetail"]["input"],
                "output": result_dict["outputDetail"]["expectedOutput"]
            }
        return {
            "statusDisplay": result_dict["statusDisplay"],
            "code": result_dict["code"],
            "lang": result_dict["lang"],
            "runtime": result_dict["runtimeDisplay"],
            "rawMemory": result_dict["memory"],
            "timestamp": result_dict["timestamp"],
        }

    if handle_fun is None:
        handle_fun = handle_response

    return general_request(LEET_CODE_BACKEND, handle_fun,
                           json={"operationName": "submissionDetails",
                                 "variables": {"submissionId": submit_id},
                                 "query": MY_SUBMISSION_DETAIL_QUERY},
                           cookies={"cookie": cookie})


async def submit_code(question_slug: str, cookie: str, lang: str,
                      leetcode_question_id: str, typed_code: str, study_plan_slug: str = None) -> dict | None:
    def handle_submit_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.text)
            return None
        result_dict = json.loads(response.text)
        return result_dict["submission_id"]

    def handle_submit_check_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.text)
            return False
        result_dict = json.loads(response.text)
        return result_dict["state"] == "SUCCESS"

    def handle_submit_detail_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.text)
            return None
        result_dict = json.loads(response.text)["data"]["submissionDetail"]
        """
        {
          "codeOutput": "",
          "expectedOutput": "",
          "input": "",
          "compileError": "",
          "runtimeError": "",
          "lastTestcase": ""
        }
        """
        return {
            "statusDisplay": result_dict["statusDisplay"],
            "outputDetail": result_dict["outputDetail"],
            "memory": result_dict["memory"],
            "memoryDisplay": result_dict["memoryDisplay"],
            "memoryPercentile": result_dict["memoryPercentile"],
            "runtimeDisplay": result_dict["runtimeDisplay"],
            "runtimePercentile": result_dict["runtimePercentile"],
            "passedTestCaseCnt": result_dict["passedTestCaseCnt"],
            "totalTestCaseCnt": result_dict["totalTestCaseCnt"],
            "code": result_dict["code"],
            "lang": result_dict["lang"],
            "timestamp": result_dict["timestamp"],
        }

    submit_request_json = {"lang": lang,
                           "question_id": leetcode_question_id,
                           "typed_code": typed_code}
    if study_plan_slug:
        submit_request_json["study_plan_slug"] = study_plan_slug
    submit_id = general_request(f"https://leetcode.cn/problems/{question_slug}/submit/", handle_submit_response,
                                json=submit_request_json,
                                cookies={"cookie": cookie},
                                headers={"Origin": "https://leetcode.cn"})
    if not submit_id:
        return None
    submit_success = False
    for _ in tqdm(range(50)):
        if general_request(f"https://leetcode.cn/submissions/detail/{submit_id}/check/",
                           handle_submit_check_response,
                           cookies={"cookie": cookie},
                           headers={"Origin": "https://leetcode.cn"}):
            submit_success = True
            break
        time.sleep(random.randint(200, 300) / 1000)
    if not submit_success:
        return None
    submit_detail = get_submission_detail(submit_id, cookie, handle_submit_detail_response)
    if submit_detail is None:
        return None
    if submit_detail["statusDisplay"] == "Accepted":
        part = SUBMIT_SUCCESS_RESULT.format(
            submit_detail["runtimeDisplay"],
            submit_detail["runtimePercentile"],
            submit_detail["memoryDisplay"],
            submit_detail["memoryPercentile"]
        )
    else:
        part = SUBMIT_FAIL_RESULT.format(
            submit_detail["outputDetail"]["input"],
            submit_detail["outputDetail"]["codeOutput"],
            submit_detail["outputDetail"]["expectedOutput"],
            submit_detail["outputDetail"]["compileError"],
            submit_detail["outputDetail"]["runtimeError"],
        )
    print(SUBMIT_BASIC_RESULT.format(
        submit_detail["statusDisplay"],
        submit_detail["passedTestCaseCnt"],
        submit_detail["totalTestCaseCnt"],
        part,
        typed_code
    ))
    return submit_detail
