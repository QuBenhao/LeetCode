import json
import traceback
import requests
import markdown
import html2text
from typing import Optional, Mapping

from query import QUESTION_INFO_QUERY, QUESTION_DESC_QUERY, QUESTION_CODE_QUERY, QUESTION_TESTCASE_QUERY, \
    QUESTION_KEYWORDS_QUERY

CATEGORY_SLUG = {"all-code-essentials","algorithms", "database"}
LANGUAGE_SLUG = {"python3", "mysql"}


def get_question_info(slug: str, cookie: Optional[str] = None) -> Optional[dict]:
    try:
        result = requests.post("https://leetcode.cn/graphql/",
                               json={"query": QUESTION_INFO_QUERY,
                                     "variables": {"titleSlug": slug},
                                     "operationName": "questionTitle"},
                               cookies={'cookie': cookie} if cookie else None)
        res_dict = json.loads(result.text)['data']['question']
        return {
            "title": res_dict['title'],
            "difficulty": res_dict['difficulty'],
            "questionFrontendId": res_dict['questionFrontendId'],
            "categoryTitle": res_dict["categoryTitle"]
        }
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_desc(slug: str, cookie: Optional[str] = None) -> Optional[str]:
    try:
        result = requests.post("https://leetcode.cn/graphql/",
                               json={
                                   "query": QUESTION_DESC_QUERY,
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionContent"},
                               cookies={'cookie': cookie} if cookie else None)
        res_dict = json.loads(result.text)['data']['question']
        return res_dict['content']
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def extract_outputs_from_md(markdown_text: str) -> list:
    backup_origin = markdown_text
    res = []
    markdown_text = "".join(markdown_text.split("Example")[1:])
    splits = markdown_text.split("Output")
    for i in range(1, len(splits)):
        tmp = (splits[i].split("\n")[0].split(">")[-1]
               .replace("null", "None")
               .replace("true", "True")
               .replace("false", "False")
               )
        tmp = tmp.strip()
        try:
            if len(tmp) > 0:
                res.append(eval(tmp))
            else:
                tmp = (splits[i].split("\n")[1].split(">")[-1]
                       .replace("null", "None")
                       .replace("true", "True")
                       .replace("false", "False"))
                res.append(eval(tmp))
        except SyntaxError as sxe:
            try:
                print(f"1. Syntax error: {sxe}, [{tmp}]")
                traceback.print_exc()
                # 将Markdown转换为HTML
                html_content = markdown.markdown(tmp)

                # 将HTML转换为字符
                text_content = html2text.html2text(html_content)
                text_content = text_content.replace("\n", "")
                res.append(eval(text_content))
            except Exception as e:
                print(f"2. Exception error: {e}, [{tmp}]")
                traceback.print_exc()
                try:
                    tmp = (splits[i].split(">")[1].split("<")[0]
                           .replace("null", "None")
                           .replace("true", "True")
                           .replace("false", "False"))

                    # 将Markdown转换为HTML
                    html_content = markdown.markdown(tmp)

                    # 将HTML转换为字符
                    text_content = html2text.html2text(html_content)
                    print(text_content)
                    text_content = text_content.replace("\n", "").strip()
                    res.append(eval(text_content))
                except Exception as ex:
                    print(f"3. Exception error: {ex}, [{tmp}]")
                    traceback.print_exc()
                    try:
                        tmp = (splits[i].split('example-io">')[1].split("<")[0]
                               .replace("null", "None")
                               .replace("true", "True")
                               .replace("false", "False"))
                        res.append(eval(tmp))
                    except Exception as exe:
                        """
                        special cases:
                        160. the node at which the two lists intersect
                        """
                        if "the node at which the two lists intersect" in backup_origin:
                            tmp = splits[i].split("\n")[0].split(">")[-1].strip()
                            if tmp == "No intersection":
                                res.append(None)
                            else:
                                res.append(eval(tmp.split("&#39;")[-2]))
                        else:
                            print(f"4. Exception error: {exe}, [{tmp}]")
                            traceback.print_exc()
                            res.append(None)
    return res


def get_question_code(slug: str, lang_slugs: list[str] = None, cookie: Optional[str] = None) -> Optional[Mapping[str, str]]:
    try:
        if lang_slugs is None:
            lang_slugs = ["python3"]
        result = requests.post("https://leetcode.cn/graphql",
                               json={
                                   "query": QUESTION_CODE_QUERY,
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionEditorData"},
                               cookies={'cookie': cookie} if cookie else None)
        res_dict = json.loads(result.text)
        code_snippets = res_dict['data']['question']['codeSnippets']
        ans = dict()
        for cs in code_snippets:
            if cs["langSlug"] in lang_slugs:
                ans[cs["langSlug"]] = cs["code"]
        return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_testcases(slug: str, lang_slug: str = "python3") -> tuple[Optional[list], str]:
    try:
        result = requests.post("https://leetcode.cn/graphql",
                               json={"query": QUESTION_TESTCASE_QUERY,
                                     "variables": {"titleSlug": slug},
                                     "operationName": "consolePanelConfig"})
        res_dict = json.loads(result.text)
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
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None, ""


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
