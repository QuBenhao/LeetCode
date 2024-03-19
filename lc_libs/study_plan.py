import heapq
import json
import traceback
from collections import defaultdict, deque

import requests


def get_user_study_plans(cookie: str) -> list | None:
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": "\n    query GetMyStudyPlan($progressType: PlanUserProgressTypeEnum!, "
                                              "$offset: Int!, $limit: Int!) {\n  studyPlanV2UserProgresses(\n    "
                                              "progressType: $progressType\n    offset: $offset\n    limit: $limit\n  )"
                                              " {\n    hasMore\n    total\n    planUserProgresses {\n      "
                                              "nextQuestionInfo {\n        inPremiumSubgroup\n        nextQuestion {\n"
                                              "          id\n          questionFrontendId\n          title\n          "
                                              "titleSlug\n          translatedTitle\n        }\n      }\n      "
                                              "nextQuestionInfo {\n        inPremiumSubgroup\n        nextQuestion {\n"
                                              "          id\n          questionFrontendId\n          title\n"
                                              "          titleSlug\n          translatedTitle\n        }\n      }\n"
                                              "      quittedAt\n      startedAt\n      plan {\n        questionNum\n"
                                              "        slug\n        premiumOnly\n        name\n        onGoing\n"
                                              "        highlight\n        cover\n      }\n      latestSubmissionAt\n"
                                              "      id\n      allCompletedAt\n      finishedQuestionNum\n    }\n  }\n}"
                                              "\n    ",
                                     "variables": {"offset": 0, "limit": 100, "progressType": "ON_GOING"},
                                     "operationName": "GetMyStudyPlan"},
                               cookies={"cookie": cookie})
        if result.text:
            res_dict = json.loads(result.text)["data"]["studyPlanV2UserProgresses"]
            ans = []
            if res_dict["total"] > 0:
                for progress in res_dict["planUserProgresses"]:
                    plan = progress["plan"]
                    if plan["onGoing"]:
                        ans.append(plan["slug"])
            if res_dict["hasMore"]:
                # TODO: LOAD MORE PLANS?
                pass
            return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None


def get_user_study_plan_progress(plan_slug: str, cookie: str, todo_num: int = 2):
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": "\n    query studyPlanProgress($slug: String!, $historyId: ID) {\n  "
                                              "studyPlanV2ProgressDetail(planSlug: $slug, id: $historyId) {\n    id\n"
                                              "    status\n    weeklyTaskScheduleResettable\n    finishedQuestionNum\n"
                                              "    studyPlanDetail {\n      questionNum\n      planSubGroups {\n   "
                                              "     slug\n        questions {\n          titleSlug\n"
                                              "          status\n        }\n      }\n    }\n  }\n}\n    ",
                                     "variables": {"slug": plan_slug},
                                     "operationName": "studyPlanProgress"},
                               cookies={"cookie": cookie})
        if result.text:
            res_dict = json.loads(result.text)["data"]["studyPlanV2ProgressDetail"]
            if res_dict["status"] == "ON_GOING":
                plan_detail = res_dict["studyPlanDetail"]
                total_num = plan_detail["questionNum"]
                finish_num = res_dict["finishedQuestionNum"]
                pq = []
                all_problems = set()
                all_solved = set()
                group_total = defaultdict(int)
                remain_problems = defaultdict(deque)
                for idx, plan_sub_group in enumerate(plan_detail["planSubGroups"]):
                    expectation = 0
                    questions = plan_sub_group["questions"]
                    group_total[idx] = len(questions)
                    do_last = []
                    for question in questions:
                        title_slug = question["titleSlug"]
                        all_problems.add(title_slug)
                        status = question["status"]
                        if status == "SOLVED":
                            all_solved.add(title_slug)
                        elif status == "PAST_SOLVED":
                            do_last.append(title_slug)
                            expectation += 0.2
                        else:
                            remain_problems[idx].append(title_slug)
                            expectation += 1
                    expectation = expectation / len(questions)
                    if expectation != 0:
                        heapq.heappush(pq, (-expectation, idx))
                    remain_problems[idx].extend(do_last)
                recommends = []
                while pq and len(recommends) < todo_num:
                    ep, idx = heapq.heappop(pq)
                    recommends.append(remain_problems[idx].popleft())
                    if len(remain_problems[idx]):
                        heapq.heappush(pq, (ep + (1.2 / group_total[idx]), idx))
                return {
                    "total": total_num,
                    "finished": finish_num,
                    "all_problems": all_problems,
                    "all_solved": all_solved,
                    "recommend": recommends
                }
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None
