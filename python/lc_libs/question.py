import ast
import json
import logging
from typing import Optional, Mapping, Tuple

import html2text
import markdown
from itertools import filterfalse

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


def safe_literal_eval(s: str):
    """
    Safely evaluate a string to a Python object using ast.literal_eval.
    Does NOT fall back to eval - literal_eval only accepts literals.

    Args:
        s: String to evaluate (must be a valid Python literal)

    Returns:
        The evaluated Python object

    Raises:
        ValueError: If the string cannot be safely evaluated
    """
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError) as e:
        logging.warning(f"Cannot safely evaluate expression: {s[:100]}...: {e}")
        raise ValueError(f"Unsafe or invalid expression: {s[:100]}...")


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
                                            lambda s: s.split("</pre>")[0].split("</strong>:")[-1].strip(),
                                            ] if not chinese else
                                           [lambda s: s.split("\n")[0].split("`")[1].strip(),
                                            lambda s: s.split("\n")[0].split(">")[-1].strip(),
                                            lambda s: s.split("\n")[1].strip(),
                                            lambda s: s.split("</pre>")[0].split("</strong>")[-1].strip(),
                                            ]):
            tmp = ""
            try:
                tmp = str_convertors(splits[i])
                evaluable_str = convert_to_evaluable_str(tmp)
                if not evaluable_str:
                    continue
                res.append(safe_literal_eval(evaluable_str))
                success_process = True
                break
            except Exception as sxe:
                logging.debug(f"{j}. Error: {sxe}, [{tmp}]", exc_info=True)
                if not tmp:
                    continue
                html_content = ""
                try:
                    # 将Markdown转换为HTML
                    html_content = markdown.markdown(tmp)

                    # 将HTML转换为字符
                    text_content = html2text.html2text(html_content)
                    text_content = convert_to_evaluable_str(text_content.replace("\n", ""))
                    res.append(safe_literal_eval(text_content))
                    success_process = True
                    break
                except Exception as e:
                    logging.debug(f"Exception error: {e}, [{html_content}]", exc_info=True)
        if success_process:
            continue
        if "the node at which the two lists intersect" in backup_origin:
            tmp = splits[i].split("\n")[0].split(">")[-1].strip()
            if tmp == "No intersection":
                res.append(None)
            else:
                try:
                    res.append(safe_literal_eval(tmp.split("&#39;")[-2]))
                except Exception:
                    res.append(None)
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
            if not lang_slugs or cs["langSlug"] in lang_slugs:
                ans[cs["langSlug"]] = cs["code"]
        return ans

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={
                               "query": QUESTION_CODE_QUERY,
                               "variables": {"titleSlug": slug},
                               "operationName": "questionEditorData"},
                           cookies={'cookie': cookie} if cookie else None)


def get_question_code_origin(slug: str, cookie: Optional[str] = None) -> list:
    def handle_response(response):
        res_dict = json.loads(response.text)
        return res_dict['data']['question']['codeSnippets']

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
                        ans.append(safe_literal_eval(input_strs[0]))
                    else:
                        ans.append([safe_literal_eval(i) for i in input_strs])
                except Exception as e:
                    logging.error(f"Unable to parse test case [{item}]: {e}", exc_info=True)
                    ans.append(None)
            elif lang_slug == "mysql":
                ans.append(item)
            else:
                logging.warning(f"Unsupported language in test cases: {lang_slug}")
        return ans, origin_data

    res = general_request(LEET_CODE_BACKEND, handle_response, json={"query": QUESTION_TESTCASE_QUERY,
                                                                    "variables": {"titleSlug": slug},
                                                                    "operationName": "consolePanelConfig"})
    if res is None:
        return res, ""
    return res


def get_questions_by_key_word(keyword: Optional[str], cookie: str,
                              category: str = "all-code-essentials",
                              fetch_all: bool = False,
                              premium_only: bool = False) -> Optional[list]:
    def handle_response(response):
        data = json.loads(response.text)
        if data["data"] is None:
            logging.error(f'cookie可能过期, 影响通过id查找题目, 错误信息: {data["errors"][0]["message"]}')
            return None
        return data["data"]["problemsetQuestionListV2"]

    ans = []
    page_size, page_no = 100, 0
    while True:
        filters = {
            "filterCombineType": "ALL",
            "statusFilter": {
                "questionStatuses": [],
                "operator": "IS"
            },
            "difficultyFilter": {
                "difficulties": [],
                "operator": "IS"
            },
            "languageFilter": {
                "languageSlugs": [],
                "operator": "IS"
            },
            "topicFilter": {
                "topicSlugs": [],
                "operator": "IS"
            },
            "acceptanceFilter": {
                # "rangeLeft": 20,
                # "rangeRight": 50
            },
            "frequencyFilter": {},
            "frontendIdFilter": {
                # "rangeLeft": 1,
                # "rangeRight": 5000
            },
            "lastSubmittedFilter": {
                # "startFrom": 1769875200,
                # "endAt": 1771689600
            },
            "publishedFilter": {
                # "startFrom": 1769875200,
                # "endAt": 1771689600
            },
            "companyFilter": {
                "companySlugs": [],
                "operator": "IS"
            },
            "positionFilter": {
                "positionSlugs": [],
                "operator": "IS"
            },
            "positionLevelFilter": {
                "positionLevelSlugs": [],
                "operator": "IS"
            },
            "contestPointFilter": {
                "contestPoints": [],
                "operator": "IS"
            },
            "premiumFilter": {
                "premiumStatus": [],
                "operator": "IS"
            }
        }
        if premium_only:
            filters["premiumFilter"]["premiumStatus"].append("PREMIUM")
        if keyword and keyword.isnumeric():
            filters["frontendIdFilter"]["rangeLeft"] = int(keyword)
            filters["frontendIdFilter"]["rangeRight"] = int(keyword)
        res_dict = general_request("https://leetcode.cn/graphql", handle_response,
                                   json={"query": QUESTION_KEYWORDS_QUERY,
                                         "variables": {
                                             "searchKeyword": keyword if keyword else "",
                                             "categorySlug": category if category in CATEGORY_SLUG
                                             else "all-code-essentials",
                                             "skip": page_no * page_size, "limit": page_size,
                                             "filters": filters
                                         },
                                         "operationName": "problemsetQuestionListV2"},
                                   cookies={'cookie': cookie} if cookie else None,
                                   headers={
                                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
                                   })
        if res_dict is None:
            return None
        ans.extend(res_dict["questions"])
        if not res_dict["hasMore"] or not fetch_all:
            break
        page_no += 1
    return ans


def get_questions_total(category: str = "all-code-essentials",
                        skip_premiums: bool = True, cookie: Optional[str] = None) -> int:
    def handle_response(response):
        data = json.loads(response.text)
        return data["data"]["problemsetQuestionListV2"]["totalLength"]

    filters = {"filterCombineType": "ALL"}
    if skip_premiums:
        filters["premiumFilter"] = {"premiumStatus": "NOT_PREMIUM"}
    result = general_request("https://leetcode.cn/graphql", handle_response,
                             json={"query": QUESTION_KEYWORDS_QUERY,
                                   "variables": {
                                       "categorySlug": category if category in CATEGORY_SLUG
                                       else "all-code-essentials",
                                       "skip": 0, "limit": 1,
                                       "filters": filters,
                                   },
                                   "operationName": "problemsetQuestionListV2"},
                             cookies={'cookie': cookie} if cookie else None)
    return result if result else 0


def get_questions_by_number(number: int, category: str = "all-code-essentials",
                            skip_premiums: bool = True, cookie: Optional[str] = None) -> Optional[list]:
    def handle_response(response):
        data = json.loads(response.text)
        return data["data"]["problemsetQuestionListV2"]["questions"]

    filters = {"filterCombineType": "ALL"}
    if skip_premiums:
        filters["premiumFilter"] = {"premiumStatus": "NOT_PREMIUM"}
    result = general_request("https://leetcode.cn/graphql", handle_response,
                             json={"query": QUESTION_KEYWORDS_QUERY,
                                   "variables": {
                                       "categorySlug": category if category in CATEGORY_SLUG
                                       else "all-code-essentials",
                                       "skip": max(0, number - 50), "limit": 100,
                                       "filters": filters
                                   },
                                   "operationName": "problemsetQuestionListV2"},
                             cookies={'cookie': cookie} if cookie else None)
    return result  # result is already the questions list from handle_response


def get_questions_by_status(status: str, category: str = "all-code-essentials", skip_premiums: bool = False,
                            skip_lcp: bool = True, cookie: Optional[str] = None) -> Optional[list]:
    def handle_response(response):
        data = json.loads(response.text)
        return data["data"]["problemsetQuestionListV2"]

    # Map old status values to new API format
    status_map = {
        "NOT_STARTED": "TO_DO",
        "TRIED": "ATTEMPTED",
        "AC": "SOLVED"
    }
    if status not in status_map:
        logging.warning(f"Unsupported question status: {status}")
        return None

    ans = []
    page_size, page_no = 100, 0
    while True:
        filters = {"filterCombineType": "ALL"}
        if skip_premiums:
            filters["premiumFilter"] = {"premiumStatus": "NOT_PREMIUM"}
        filters["statusFilter"] = {"questionStatuses": [status_map[status]]}
        res_dict = general_request("https://leetcode.cn/graphql", handle_response,
                                   json={"query": QUESTION_KEYWORDS_QUERY,
                                         "variables": {
                                             "categorySlug": category if category in CATEGORY_SLUG
                                             else "all-code-essentials",
                                             "skip": page_no * page_size, "limit": page_size,
                                             "filters": filters,
                                         },
                                         "operationName": "problemsetQuestionListV2"},
                                   cookies={'cookie': cookie} if cookie else None)
        if res_dict is None:
            return None
        logging.debug(res_dict["questions"])
        ans.extend(
            filterfalse(lambda x: skip_lcp and x["questionFrontendId"].startswith("LCP "),
                        res_dict["questions"]))
        if not res_dict["hasMore"]:
            break
        page_no += 1
    return ans
