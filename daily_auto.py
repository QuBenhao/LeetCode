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


def extract_outputs_from_md(markdown_text: str) -> list:
    res = []
    splits = markdown_text.split("Output")
    for i in range(1, len(splits), 2):
        res.append(eval(splits[i].split("\n")[1].split(">")[-1].replace("null", "None")))
    return res


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


def get_question_testcases(slug: str) -> list | None:
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
            input_strs = item.replace("null", "None").split("\n")
            if len(input_strs) == 1:
                ans.append(eval(input_strs[0]))
            else:
                ans.append([eval(i) for i in input_strs])
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
                f.write('import solution\n')
                f.write("from typing import *\n\n\n")
                f.write(f'class Solution(solution.Solution):\n')
                f.write('    def solve(self, test_input=None):\n')
                f.write('        pass\n\n\n')
                f.write(code)
                f.write("\n")
        if desc is not None:
            testcases = get_question_testcases(sg)
            outputs = extract_outputs_from_md(desc)
            if testcases is not None:
                with open(f"{dir_path}/testcase.py", "w") as f:
                    f.write('from collections import namedtuple\n')
                    f.write('import testcase\n\n')
                    f.write('case = namedtuple("Testcase", ["Input", "Output"])\n\n\n')
                    f.write('class Testcase(testcase.Testcase):\n')
                    f.write('\tdef __init__(self):\n')
                    f.write('\t\tself.testcases = []\n')
                    for inputs, outputs in zip(testcases, outputs):
                        f.write(f'\t\tself.testcases.append(case(Input={inputs}, Output={outputs}))\n')
                    f.write('\n\tdef get_testcases(self):\n')
                    f.write('\t\treturn self.testcases\n')
    else:
        print("solved before")
    with open(f"test.py", "r") as f:
        lines = f.readlines()
    with open("test.py", "w") as f:
        for line in lines:
            if line.startswith("QUESTION ="):
                line = "QUESTION = \"{}\"\n".format(daily_info["questionId"])
            f.write(line)
    sys.exit(0)
