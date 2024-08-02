SAN_YE_SOLUTIONS_URL = "https://github.com/SharingSource/LogicStack-LeetCode/blob/main/LeetCode/"
from python.utils.str_util import back_question_id
import requests
import json



def get_answer_san_ye(problem_id: int) -> str:
    origin_id = back_question_id(str(problem_id))
    if origin_id.isnumeric():
        num = int(origin_id)
        rg = (num - 1) // 10 * 10
        folder = f"{rg + 1}-{rg + 10}"
    else:
        if origin_id.startswith("LCR "):
            pass
