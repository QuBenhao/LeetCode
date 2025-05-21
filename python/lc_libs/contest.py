import ast
import json
import logging
import re
from typing import List

from bs4 import BeautifulSoup

from python.constants import CONTEST_HISTORY_QUERY, LEET_CODE_BACKEND
from python.utils import general_request


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
        code_info = soup.find("script", string=re.compile("var pageData ="))
        if not code_info:
            logging.warning("Cookie might be expired! Please update the cookie and try again.")
            return None
        code_info_str = code_info.decode_contents()
        en_title = None
        cn_title = None
        example_testcases = ""
        sample_test_case = ""
        code_definitions = None
        for line in code_info_str.split("\n"):
            if "questionSourceTitle" in line:
                en_title = re.search(r"questionSourceTitle: '(.*?)'", line).group(1)
                continue
            if "questionTitle" in line:
                cn_title = line.split("'")[-2]
                continue
            if "questionExampleTestcases" in line:
                qet = re.search(r"questionExampleTestcases: '(.*)'", line).group(1)
                decoded_str = qet.encode('latin-1').decode('unicode_escape')
                example_testcases = decoded_str
                continue
            if "sampleTestCase" in line:
                sample_test_case = re.search(r"sampleTestCase: '(.*)'", line).group(1)
                decoded_str = sample_test_case.encode('latin-1').decode('unicode_escape')
                sample_test_case = decoded_str
                continue
            if "codeDefinition" in line:
                code_definitions = line.split(":", 1)[1].rsplit(",", 1)[0]
                # """ in decoded_str
                code_definitions = ast.literal_eval(code_definitions)
                continue
        input_vars = sample_test_case.count("\n") + 1
        question_example_testcases = []
        splits = example_testcases.split("\n")
        for inputs in range(0, len(splits), input_vars):
            cur_inputs = []
            for i in range(inputs, inputs + input_vars):
                cur_inputs.append(json.loads(splits[i]))
            question_example_testcases.append(cur_inputs)

        language_default_code = {}
        for code_definition in code_definitions:
            if code_definition.get("value") not in languages:
                continue
            language_default_code[code_definition.get("value")] = code_definition.get("defaultCode")

        title = soup.find("h3")
        question_id = title.text.split(".")[0]

        cn_question_content = soup.find("div", class_="question-content default-content")
        if cn_question_content:
            cn_markdown_content = f"# {question_id}. {cn_title}\n\n{cn_question_content.decode_contents()}"
        else:
            logging.warning("No CN content found for %s", question_slug)
            cn_markdown_content = None
        en_question_content = soup.find("div", class_="question-content source-content")
        if en_question_content:
            en_markdown_content = f"# {question_id}. {en_title}\n\n{en_question_content.decode_contents()}"
        else:
            logging.warning("No EN content found for %s", question_slug)
            en_markdown_content = None
        outputs = cn_question_content.find_all("span", class_="example-io")
        example_outputs = []
        for output in outputs[1::2]:
            example_outputs.append(json.loads(output.text))
        return {
            "question_id": question_id,
            "title": title.text,
            "question_slug": question_slug,
            "en_markdown_content": en_markdown_content,
            "cn_markdown_content": cn_markdown_content,
            "question_example_testcases": question_example_testcases,
            "question_example_testcases_output": example_outputs,
            "language_default_code": language_default_code
        }

    url = f"https://leetcode.cn/contest/{contest_id}/problems/{question_slug}/"
    return general_request(url, handle_response, "get", cookies={"cookie": cookie})
