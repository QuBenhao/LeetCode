import argparse
import os
import traceback
import sys

from dotenv import load_dotenv

from constants import constant
from lc_libs.submission import check_accepted_submission_all
from utils import get_default_folder

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, type=str, help='The user slug in LeetCode.')
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    push_key = os.getenv(constant.PUSH_KEY)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())

    res = check_accepted_submission_all(cke)
    print(res)
    sys.exit(0)
