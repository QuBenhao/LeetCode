import logging
import json
import os
from pathlib import Path
import sys
import unittest
from importlib.util import spec_from_file_location, module_from_spec

from dotenv import load_dotenv
import constants
from utils import get_default_folder, timeout

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
        question = daily_json.get("daily", None)
        if not question:
            self.fail(f"Daily problem not found for folder: {problem_folder}, please check daily-{problem_folder}.json")
        logging.info(f"Testing problem: {question}")

        problem_path = root_path / problem_folder / f"{problem_folder}_{question}"
        if not problem_path.exists():
            logging.warning("[QUESTION: {}] not found under problem folder: {}".format(question, problem_folder))
            problem_folder = get_default_folder(paid_only=True)
            problem_path = root_path / problem_folder / f"{problem_folder}_{question}"
        self.assertTrue(problem_path.exists(), msg="Please set up the problem env first!")

        solution_spec = spec_from_file_location("module.name", str(problem_path / "solution.py"))
        solution = module_from_spec(solution_spec)
        solution_spec.loader.exec_module(solution)
        solution_obj = solution.Solution()

        testcase_spec = spec_from_file_location("module.name", str(problem_path / "testcase.py"))
        testcase = module_from_spec(testcase_spec)
        testcase_spec.loader.exec_module(testcase)
        testcase_obj = testcase.Testcase()

        if not testcase_obj.get_testcases():
            self.fail(f"No testcases found in [{question}] testcase.py")

        for test in testcase_obj.get_testcases():
            with self.subTest(f"testcase: {test}", testcase=test):
                i, o = test
                try:
                    result = exec_solution(solution_obj, i)
                except TimeoutError as _:
                    self.fail("Solution timeout in 3s, input: {}".format(i))
                if o is not None:
                    self.assertIsNotNone(result, f"input = {i}, No solution")
                try:
                    if o and isinstance(o, list):
                        if isinstance(o[0], float):
                            for v1, v2 in zip(o, result):
                                self.assertAlmostEqual(v1, v2, msg=f"input = {i}", delta=0.00001)
                        elif all(x is not None for x in o) and (
                                isinstance(o[0], list) or isinstance(o[0], set)) and not any(None in x for x in o):
                            self.assertListEqual(sorted(sorted(item) for item in o),
                                                 sorted(sorted(item) for item in result), msg=f"input = {i}")
                        else:
                            self.assertListEqual(o, result, msg=f"input = {i}")
                    elif result and isinstance(result, list):
                        self.assertEqual(o, result[0], msg=f"input = {i}")
                    else:
                        if isinstance(o, float):
                            self.assertAlmostEqual(o, result, msg=f"input = {i}", delta=0.00001)
                        elif isinstance(o, set) and result and not isinstance(result, set):
                            self.assertIn(result, o, msg=f"input = {i}")
                        else:
                            self.assertEqual(o, result, msg=f"input = {i}")
                except AssertionError as ae:
                    last = result
                    result = solution_obj.solve(test_input=i)
                    if last != result:
                        loop_times = 10000
                        for idx in range(loop_times):
                            try:
                                if isinstance(o, list):
                                    self.assertListEqual(o, result)
                                else:
                                    self.assertEqual(o, result)
                                logging.info(f"Meet expect output in {idx + 2} loop: {result}")
                                break
                            except AssertionError as _:
                                result = solution_obj.solve(test_input=i)
                        if isinstance(o, list):
                            self.assertListEqual(o, result, msg=f"input={i}, "
                                                                f"Random case not happened in {loop_times + 2} times!")
                        else:
                            self.assertEqual(o, result, msg=f"input={i}, "
                                                            f"Random case not happened in {loop_times + 2} times!")
                    else:
                        raise ae


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
