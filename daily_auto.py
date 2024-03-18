import json
import os.path
import sys
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


def get_question_desc(slug: str) -> str | None:
    try:
        result = requests.post("https://leetcode.cn/graphql/",
                               json={
                                   "query": "\n    query questionContent($titleSlug: String!) {\n  "
                                            "question(titleSlug: $titleSlug) {\n    content\n    editorType\n    "
                                            "mysqlSchemas\n    dataSchemas\n  }\n}\n    ",
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionContent"})
        res_dict = json.loads(result.text)
        return res_dict['data']['question']['content']
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_code(slug: str) -> str | None:
    try:
        result = requests.post("https://leetcode.cn/graphql",
                               json={
                                   "query": "\n    query questionEditorData($titleSlug: String!) {\n  "
                                            "question(titleSlug: $titleSlug) {\n    questionId\n    "
                                            "questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      "
                                            "code\n    }\n    envInfo\n    enableRunCode\n    hasFrontendPreview\n    "
                                            "frontendPreviews\n  }\n}\n    ",
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionEditorData"})
        res_dict = json.loads(result.text)
        code_snippets = res_dict['data']['question']['codeSnippets']
        for cs in code_snippets:
            if cs["langSlug"] == "python3":
                return cs["code"]
        return None
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_testcases(slug: str) -> list[tuple] | None:
    try:
        result = requests.post("https://leetcode.cn/graphql",
                               json={"query": "\n    query consolePanelConfig($titleSlug: String!) {\n"
                                              "  question(titleSlug: $titleSlug) {\n    questionId\n"
                                              "    questionFrontendId\n    questionTitle\n    enableRunCode\n    "
                                              "enableSubmit\n    enableTestMode\n    jsonExampleTestcases\n    "
                                              "exampleTestcases\n    metaData\n    sampleTestCase\n  }\n}\n    ",
                                     "variables": {"titleSlug": slug},
                                     "operationName": "consolePanelConfig"})
        res_dict = json.loads(result.text)
        ans = []
        json_testcase = json.loads(res_dict["data"]["question"]["jsonExampleTestcases"])
        for item in json_testcase:
            input_case, output_case = item.split("\n")
            # Skip the quotation marks enclosing the case
            test_input = eval(input_case)
            test_output = eval(output_case)
            ans.append((test_input, test_output))
        return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


if __name__ == '__main__':
    daily_info = get_daily_question()
    if not daily_info:
        sys.exit(1)
    dir_path = "problems/{}".format(daily_info['questionId'])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        sg = daily_info['questionSlug']
        desc = get_question_desc(sg)
        if desc is not None:
            with open(f"{dir_path}/problem.md", "w") as f:
                f.write("# {}. {}\n\n{}".format(daily_info['questionId'], daily_info['questionNameEn'], desc))
        code = get_question_code(sg)
        if code is not None:
            with open(f"{dir_path}/solution.py", "w") as f:
                f.write('import solution\n\n')
                f.write(f'class Solution(solution.Solution):\n')
                f.write('\tdef solve(self, test_input=None):\n')
                f.write('\t\tpass\n\n\n')
                f.write("from typing import *\n")
                f.write(code)
        testcases = get_question_testcases(sg)
        if testcases is not None:
            with open(f"{dir_path}/testcase.py", "w") as f:
                f.write('from collections import namedtuple\n')
                f.write('import testcase\n\n')
                f.write('case = namedtuple("Testcase", ["Input", "Output"])\n\n\n')
                f.write('class Testcase(testcase.Testcase):\n')
                f.write('\tdef __init__(self):\n')
                f.write('\t\tself.testcases = []\n')
                for ip, op in testcases:
                    f.write(f'\t\tself.testcases.append(case(Input={ip}, Output={op}))\n')
                f.write('\n\tdef get_testcases(self):\n')
                f.write('\t\treturn self.testcases\n')
    else:
        print("solved before")
    sys.exit(0)
