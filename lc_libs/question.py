import json
import traceback

import requests


def get_question_info(slug: str) -> dict | None:
    try:
        result = requests.post("https://leetcode.cn/graphql/",
                               json={"query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug:"
                                              " $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n"
                                              "    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n"
                                              "    categoryTitle\n  }\n}\n    ",
                                     "variables": {"titleSlug": slug},
                                     "operationName": "questionTitle"})
        res_dict = json.loads(result.text)['data']['question']
        return {
            "title": res_dict['title'],
            "difficulty": res_dict['difficulty'],
            "questionFrontendId": res_dict['questionFrontendId'],
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
    for i in range(1, len(splits)):
        tmp = splits[i].split("\n")[0].split(">")[-1].replace("null", "None")
        tmp = tmp.strip()
        if len(tmp) > 0:
            res.append(eval(tmp))
        else:
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
