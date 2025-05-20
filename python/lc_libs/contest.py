import ast
import json
import re
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md

import dotenv

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


def get_contest_problem_info(contest_id: str, question_slug: str, cookie: str):
    # url = f"https://leetcode.cn/contest/{contest_id}/problems/{question_slug}/"
    # resp = requests.get(url, timeout=5, cookies={"LEETCODE_SESSION": cookie})
    with open("../dev/example_question.html", "r", encoding="utf-8") as f:
        text = f.read()
    soup = BeautifulSoup(text, "html.parser")
    code_info = soup.find("script", string=re.compile("var pageData ="))
    code_info_str = code_info.decode_contents()
    en_title = None
    question_example_testcases = []
    code_definitions = None
    for line in code_info_str.split("\n"):
        if "questionSourceTitle" in line:
            en_title = re.search(r"questionSourceTitle: '(.*?)'", line).group(1)
            continue
        if "questionExampleTestcases" in line:
            qet = re.search(r"questionExampleTestcases: '(.*)'", line).group(1)
            decoded_str = qet.encode('latin-1').decode('unicode_escape').split("\n")
            for s in decoded_str:
                question_example_testcases.append(json.loads(s))
            continue
        if "codeDefinition" in line:
            code_definitions = line.split(":", 1)[1].rsplit(",", 1)[0]
            # """ in decoded_str
            code_definitions = ast.literal_eval(code_definitions)
            continue

    print(code_definitions[3].get("defaultCode"))

    title = soup.find("h3")
    question_id = title.text.split(".")[0]

    cn_question_content = soup.find("div", class_="question-content default-content")
    if cn_question_content:
        cn_markdown_content = f"# {md(title.decode_contents())}\n\n{md(cn_question_content.decode_contents())}"
    else:
        print("No CN content found")
    en_question_content = soup.find("div", class_="question-content source-content")
    if en_question_content:
        en_markdown_content = f"# {question_id}. {en_title}\n\n{md(en_question_content.decode_contents())}"
    else:
        print("No EN content found")


if __name__ == "__main__":
    dotenv.load_dotenv()
    get_contest_info(contest_id="biweekly-contest-155")
    time.sleep(5)
    # get_contest_problem_info(contest_id="biweekly-contest-155", question_slug="find-the-most-common-response", cookie=None)
