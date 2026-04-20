import json
import logging
import os
from pathlib import Path
import sys
import unittest
from importlib.util import spec_from_file_location, module_from_spec

import constants
from dotenv import load_dotenv
from python.utils import get_default_folder, timeout, resolve_link, assert_result, run_with_retry_on_random

logging.basicConfig(level=logging.INFO, format=constants.LOGGING_FORMAT, datefmt=constants.DATE_FORMAT)


class Test(unittest.TestCase):
    def test(self):
        @timeout()
        def exec_solution(sol, ipt):
            return sol.solve(test_input=ipt)

        load_dotenv()
        root_path = Path(__file__).parent.parent.resolve()
        problem_folder = os.getenv(constants.PROBLEM_FOLDER, None)
        if not problem_folder:
            problem_folder = get_default_folder()

        json_file = root_path / f"daily-{problem_folder}.json"
        with json_file.open("r", encoding="utf-8") as json_file:
            daily_json = json.loads(json_file.read())
        plans = daily_json.get("plans", None)

        logging.info(f"Testing problems: {plans[0::2]}")

        for i in range(0, len(plans), 2):
            q, folder = plans[i], plans[i + 1]
            with self.subTest(f"[{q}]", question=q):
                problem_path = root_path / folder / f"{folder}_{q}"
                if not problem_path.exists():
                    logging.warning("[QUESTION: {}] not found under problem folder: {}".format(q, problem_path))
                    tmp_folder = get_default_folder(paid_only=True)
                    problem_path = root_path / tmp_folder / f"{tmp_folder}_{q}"
                self.assertTrue(problem_path.exists(), msg="Please set up the problem env first!")

                # Resolve link if exists
                solution_path, link_info = resolve_link(problem_path)
                if link_info:
                    logging.info(f"Problem {q} is linked to {link_info['link_to']}: {link_info.get('reason', 'No reason provided')}")

                solution_spec = spec_from_file_location("module.name", str(solution_path / "solution.py"))
                solution = module_from_spec(solution_spec)
                solution_spec.loader.exec_module(solution)
                solution_obj = solution.Solution()

                testcase_spec = spec_from_file_location("module.name", str(problem_path / "testcase.py"))
                testcase = module_from_spec(testcase_spec)
                testcase_spec.loader.exec_module(testcase)
                testcase_obj = testcase.Testcase()
                if not testcase_obj.get_testcases():
                    self.fail(f"No testcases found in [{q}] testcase.py")

                total = len(testcase_obj.get_testcases())
                for idx, test in enumerate(testcase_obj.get_testcases(), 1):
                    with self.subTest(f"[{q}] case {idx}/{total}", testcase=test):
                        ipt, expected = test
                        logging.info("Testing problem: {}, input: {}".format(q, ipt))
                        try:
                            result = exec_solution(solution_obj, ipt)
                        except TimeoutError as _:
                            self.fail("Solution timeout in 3s, input: {}".format(ipt))
                        try:
                            assert_result(self, expected, result, problem_id=q, input_value=ipt)
                        except AssertionError as ae:
                            last = result
                            result = solution_obj.solve(test_input=ipt)
                            if last != result:
                                result, success = run_with_retry_on_random(solution_obj, ipt, expected)
                                if success:
                                    logging.info(f"Meet expect output after retry: {result}")
                                else:
                                    if isinstance(expected, list):
                                        self.assertListEqual(expected, result,
                                                             msg=f"problem: {q}, input = {ipt}, Random case not happened!")
                                    else:
                                        self.assertEqual(expected, result,
                                                         msg=f"problem: {q}, input = {ipt}, Random case not happened!")
                            else:
                                raise ae


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
