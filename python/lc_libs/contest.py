import json
import logging
from typing import List

from bs4 import BeautifulSoup

from python.constants import CONTEST_HISTORY_QUERY, LEET_CODE_BACKEND
from python.lc_libs import extract_outputs_from_md
from python.utils import general_request
from python.utils.str_util import decode_unicode_string


def get_contest_list(page_num: int = 1, page_size: int = 10):
    def handle_response(response):
        res_dict = json.loads(response.text)
        data = res_dict['data']["contestHistory"]
        contests = data['contests']
        contest_list = []
        for contest in contests:
            contest_list.append({
                "title": contest["title"],
                "title_slug": contest["titleSlug"],
                "start_time": contest["startTime"],
            })
        return {
            "total": data["totalNum"],
            "contests": contest_list,
            "has_more": data["totalNum"] > page_num * page_size
        }

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={"operationName": "contestHistory",
                                 "query": CONTEST_HISTORY_QUERY,
                                 "variables": {"pageNum": page_num, "pageSize": page_size}})


def get_contest_info(contest_id: str):
    def handle_response(response):
        data = response.json()
        questions = data.get("questions", [])
        question_list = []
        for question in questions:
            question_list.append({
                "title": question["title"],
                "title_slug": question["title_slug"],
                "english_title": question["english_title"],
            })
        return question_list

    url = f"https://leetcode.cn/contest/api/info/{contest_id}/"
    return general_request(url, handle_response, "get")



def get_contest_problem_info(contest_id: str, question_slug: str, languages: List[str], cookie: str):
    def handle_response(response):
        logging.debug(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        code_info = soup.find("script", id="__NEXT_DATA__")
        if not code_info:
            logging.warning("Cookie might be expired! Please update the cookie and try again.")
            return None
        code_info_str = code_info.decode_contents()
        code_info_json = json.loads(code_info_str)
        question_json = code_info_json["props"]["pageProps"]["dehydratedState"]["queries"][1]["state"]["data"]["contestQuestion"]["question"]
        question_id = question_json["questionFrontendId"]
        en_title = question_json["title"]
        cn_title = question_json["translatedTitle"]

        en_markdown = decode_unicode_string(question_json["content"]) 
        en_markdown_content = f"# {question_id}. {en_title}\n\n{en_markdown}"
        cn_markdown = decode_unicode_string(question_json["translatedContent"])
        cn_markdown_content = f"# {question_id}. {cn_title}\n\n{cn_markdown}"

        example_testcase_list = question_json["exampleTestcaseList"]
        question_example_testcases = []
        for example_testcase_str in example_testcase_list:
            lt = example_testcase_str.split("\n")
            cur = []
            for part in lt:
                cur.append(json.loads(part))
            question_example_testcases.append(cur)

        example_outputs = extract_outputs_from_md(en_markdown_content)

        code_snippets = question_json["codeSnippets"]
        language_default_code = {}
        for code_snippet in code_snippets:
            if code_snippet["langSlug"] in languages:
                language_default_code[code_snippet["langSlug"]] = code_snippet["code"]
    
        return {
            "question_id": question_id,
            "title": en_title,
            "question_slug": question_slug,
            "en_markdown_content": en_markdown_content,
            "cn_markdown_content": cn_markdown_content,
            "question_example_testcases": question_example_testcases,
            "question_example_testcases_output": example_outputs,
            "language_default_code": language_default_code
        }

    url = f"https://leetcode.cn/contest/{contest_id}/problems/{question_slug}/description"
    return general_request(url, handle_response, "get", cookies={"cookie": cookie})
