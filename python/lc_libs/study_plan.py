import heapq
import json
import logging
from collections import defaultdict, deque
from typing import Optional

import requests

from python.constants import LEET_CODE_BACKEND, PLAN_QUERY, PLAN_PROGRESS_QUERY
from python.utils import general_request, get_cur_weekday


def get_user_study_plans(cookie: str) -> Optional[list]:
    def handle_response(response: requests.Response):
        if response.text:
            res_dict = json.loads(response.text)["data"]["studyPlanV2UserProgresses"]
            ans = []
            if not res_dict:
                logging.warning("Cookie might be expired! Please update the cookie and try again.")
                return None
            if res_dict["total"] > 0:
                for progress in res_dict["planUserProgresses"]:
                    plan = progress["plan"]
                    if plan["onGoing"]:
                        ans.append(plan["slug"])
            if res_dict["hasMore"]:
                # TODO: LOAD MORE PLANS?
                pass
            return ans
        return None

    return general_request(LEET_CODE_BACKEND,
                           handle_response,
                           json={"query": PLAN_QUERY,
                                 "variables": {"offset": 0, "limit": 100, "progressType": "ON_GOING"},
                                 "operationName": "GetMyStudyPlan"},
                           cookies={"cookie": cookie})


def generate_question_todo(plan_sub_groups, todo_num: int):
    pq = []
    all_problems = set()
    all_solved = set()
    group_total = defaultdict(int)
    remain_problems = defaultdict(deque)
    for idx, plan_sub_group in enumerate(plan_sub_groups):
        expectation = 0
        premium = plan_sub_group["premiumOnly"]
        questions = plan_sub_group["questions"]
        if not questions:
            continue
        group_total[idx] = len(questions)
        do_first_new = []
        do_first_before = []
        normal = []
        do_last = []
        for question in questions:
            title_slug = question["titleSlug"]
            all_problems.add(title_slug)
            status = question["status"]
            paid_only = question["paidOnly"]
            if status == "SOLVED":
                all_solved.add(title_slug)
            elif status == "PAST_SOLVED":
                if paid_only:
                    do_first_before.append(title_slug)
                    expectation += 0.1
                else:
                    do_last.append(title_slug)
                expectation += 0.2
            else:
                if paid_only:
                    do_first_new.append(title_slug)
                    expectation += 0.5
                else:
                    normal.append(title_slug)
                expectation += 1
        expectation = expectation / len(questions)
        if expectation != 0:
            heapq.heappush(pq, (-expectation * (100 if premium else 1), idx))
        remain_problems[idx].extend(do_first_new)
        remain_problems[idx].extend(do_first_before)
        remain_problems[idx].extend(normal)
        remain_problems[idx].extend(do_last)
    recommends = []
    while pq and len(recommends) < todo_num:
        ep, idx = heapq.heappop(pq)
        recommends.append(remain_problems[idx].popleft())
        if len(remain_problems[idx]):
            heapq.heappush(pq, (ep + (1.2 / group_total[idx]), idx))
    return all_problems, all_solved, recommends


def get_user_study_plan_progress(plan_slug: str, cookie: str, todo_num: int = -1):
    if todo_num < 0:
        cur_weekday = get_cur_weekday()
        todo_num = 0 if cur_weekday < 5 else 1

    def handle_response(response: requests.Response):
        if response.text:
            res_dict = json.loads(response.text)["data"]["studyPlanV2ProgressDetail"]
            if res_dict["status"] == "ON_GOING":
                plan_detail = res_dict["studyPlanDetail"]
                total_num = plan_detail["questionNum"]
                finish_num = res_dict["finishedQuestionNum"]
                all_problems, all_solved, recommends = generate_question_todo(plan_detail["planSubGroups"], todo_num)
                return {
                    "total": total_num,
                    "finished": finish_num,
                    "all_problems": all_problems,
                    "all_solved": all_solved,
                    "recommend": recommends
                }
        return None

    return general_request(LEET_CODE_BACKEND,
                           handle_response,
                           json={"query": PLAN_PROGRESS_QUERY,
                                 "variables": {"slug": plan_slug},
                                 "operationName": "studyPlanProgress"},
                           cookies={"cookie": cookie})
