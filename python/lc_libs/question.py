import json
import traceback
from typing import Optional, Mapping, Tuple

import html2text
import markdown
import requests

from python.constants import (LEET_CODE_BACKEND, QUESTION_INFO_QUERY, QUESTION_DESC_QUERY, QUESTION_DESC_CN_QUERY,
                              QUESTION_CODE_QUERY, QUESTION_TESTCASE_QUERY, QUESTION_KEYWORDS_QUERY)
from python.utils import general_request, format_question_id

CATEGORY_SLUG = {"all-code-essentials", "algorithms", "database"}
LANGUAGE_SLUG = {"python3", "mysql"}


def get_question_info(slug: str, cookie: Optional[str] = None) -> Optional[dict]:
    def handle_response(response):
        res_dict = json.loads(response.text)['data']['question']
        return {
            "title": res_dict['title'],
            "difficulty": res_dict['difficulty'],
            "questionFrontendId": format_question_id(res_dict['questionFrontendId']),
            "categoryTitle": res_dict["categoryTitle"],
            "questionId": res_dict["questionId"],
            "isPaidOnly": res_dict["isPaidOnly"]
        }

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={"query": QUESTION_INFO_QUERY,
                                 "variables": {"titleSlug": slug},
                                 "operationName": "questionTitle"},
                           cookies={'cookie': cookie} if cookie else None)


def get_question_desc(slug: str, cookie: Optional[str] = None) -> Optional[str]:
    def handle_response(response):
        res_dict = json.loads(response.text)['data']['question']
        return res_dict['content']

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={
                               "query": QUESTION_DESC_QUERY,
                               "variables": {"titleSlug": slug},
                               "operationName": "questionContent"},
                           cookies={'cookie': cookie} if cookie else None)


def get_question_desc_cn(slug: str, cookie: Optional[str] = None) -> Optional[Tuple[str, str]]:
    def handle_response(response):
        res_dict = json.loads(response.text)['data']['question']
        return res_dict['translatedContent'], res_dict['translatedTitle']

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={"query": QUESTION_DESC_CN_QUERY,
                                 "variables": {"titleSlug": slug},
                                 "operationName": "questionTranslations"},
                           cookies={'cookie': cookie} if cookie else None)


def convert_to_evaluable_str(s: str) -> str:
    """
    This function replaces certain words in the input string to make it evaluable.
    Values like null, true and false are replaced with their python equivalents : None, True, False
    """
    evaluable_str = s.replace("null", "None").replace("true", "True").replace("false", "False")
    if evaluable_str.startswith("[") and evaluable_str.endswith("]"):
        if any(v == "#" for v in evaluable_str.split(",")):
            evaluable_str = evaluable_str.replace("#", "None")
    return evaluable_str


def extract_outputs_from_md(markdown_text: str, chinese: bool = False) -> list:
    backup_origin = markdown_text
    res = []
    markdown_text = "".join(markdown_text.split("Example")[1:]) if not chinese else "".join(
        markdown_text.split("示例")[1:])
    splits = markdown_text.split("Output") if not chinese else markdown_text.split("输出")
    for i in range(1, len(splits)):
        success_process = False
        for j, str_convertors in enumerate([lambda s: s.split("\n")[0].split(">")[-1].strip(),
                                            lambda s: s.split("\n")[1].split(">")[-1].strip(),
                                            lambda s: s.split(">")[1].split("<")[0].strip(),
                                            lambda s: s.split('</span>')[0].split(">")[-1].strip(),
                                            lambda s: s.split('example-io">')[1].split("<")[0].strip(),
                                            ] if not chinese else
                                           [lambda s: s.split("\n")[0].split("`")[1].strip(),
                                            ]):
            tmp = ""
            try:
                tmp = str_convertors(splits[i])
                evaluable_str = convert_to_evaluable_str(tmp)
                if not evaluable_str:
                    continue
                res.append(eval(evaluable_str))
                success_process = True
                break
            except Exception as sxe:
                print(f"{j}. Error: {sxe}, [{tmp}]")
                traceback.print_exc()
                if not tmp:
                    continue
                html_content = ""
                try:
                    # 将Markdown转换为HTML
                    html_content = markdown.markdown(tmp)

                    # 将HTML转换为字符
                    text_content = html2text.html2text(html_content)
                    text_content = convert_to_evaluable_str(text_content.replace("\n", ""))
                    res.append(eval(text_content))
                    success_process = True
                    break
                except Exception as e:
                    print(f"Exception error: {e}, [{html_content}]")
                    traceback.print_exc()
        if success_process:
            continue
        if "the node at which the two lists intersect" in backup_origin:
            tmp = splits[i].split("\n")[0].split(">")[-1].strip()
            if tmp == "No intersection":
                res.append(None)
            else:
                res.append(eval(tmp.split("&#39;")[-2]))
        else:
            res.append(None)

    return res


def get_question_code(slug: str,
                      lang_slugs: list[str] = None,
                      cookie: Optional[str] = None
                      ) -> Optional[Mapping[str, str]]:
    def handle_response(response):
        res_dict = json.loads(response.text)
        code_snippets = res_dict['data']['question']['codeSnippets']
        ans = dict()
        for cs in code_snippets:
            if cs["langSlug"] in lang_slugs:
                ans[cs["langSlug"]] = cs["code"]
        return ans

    if lang_slugs is None:
        lang_slugs = ["python3"]
    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={
                               "query": QUESTION_CODE_QUERY,
                               "variables": {"titleSlug": slug},
                               "operationName": "questionEditorData"},
                           cookies={'cookie': cookie} if cookie else None)


def get_question_testcases(slug: str, lang_slug: str = "python3") -> tuple[Optional[list], str]:
    def handle_response(response):
        res_dict = json.loads(response.text)
        ans = []
        origin_data = res_dict["data"]["question"]["jsonExampleTestcases"]
        json_testcase = json.loads(origin_data)
        for item in json_testcase:
            if lang_slug == "python3":
                input_strs = item.replace("null", "None").split("\n")
                try:
                    if len(input_strs) == 1:
                        ans.append(eval(input_strs[0]))
                    else:
                        ans.append([eval(i) for i in input_strs])
                except Exception as ex:
                    print("Exception caught: ", ex)
                    traceback.print_exc()
                    ans.append(None)
            elif lang_slug == "mysql":
                ans.append(item)
            else:
                print("Unsupported language")
        return ans, origin_data

    res = general_request(LEET_CODE_BACKEND, handle_response, json={"query": QUESTION_TESTCASE_QUERY,
                                                                    "variables": {"titleSlug": slug},
                                                                    "operationName": "consolePanelConfig"})
    if res is None:
        return res, ""
    return res


def get_questions_by_key_word(keyword: Optional[str],
                              category: str = "all-code-essentials",
                              fetch_all: bool = False,
                              premium_only: bool = False) -> Optional[list]:
    try:
        ans = []
        page_size, page_no = 50, 0
        while True:
            filters = dict()
            if keyword:
                filters["searchKeywords"] = keyword
            if premium_only:
                filters["premiumOnly"] = premium_only
            result = requests.post("https://leetcode.cn/graphql",
                                   json={"query": QUESTION_KEYWORDS_QUERY,
                                         "variables": {
                                             "categorySlug": category if category in CATEGORY_SLUG
                                             else "all-code-essentials",
                                             "skip": page_no * page_size, "limit": page_size,
                                             "filters": filters
                                         },
                                         "operationName": "problemsetQuestionList"})
            res_dict = json.loads(result.text)["data"]["problemsetQuestionList"]
            ans.extend(res_dict["questions"])
            if not res_dict["hasMore"] or not fetch_all:
                break
            page_no += 1
        return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None
