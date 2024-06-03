import os.path
import sys
import unittest
from importlib.util import spec_from_file_location, module_from_spec

import constants
from dotenv import load_dotenv
from utils import get_default_folder

# Question ID that wants to test, modify here as passing arguments
QUESTIONS = ['1275', '459']


class Test(unittest.TestCase):
    def test(self):
        load_dotenv()
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        problem_folder = os.getenv(constants.PROBLEM_FOLDER, get_default_folder())

        print(f"Testing problems: {QUESTIONS}")

        for q in QUESTIONS:
            with self.subTest(f"Testing problem: {q}", question=q):
                problem_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{q}")
                self.assertTrue(os.path.exists(problem_path), msg="Please set up the problem env first!")

                solution_spec = spec_from_file_location("module.name", f"{problem_path}/solution.py")
                solution = module_from_spec(solution_spec)
                solution_spec.loader.exec_module(solution)
                solution_obj = solution.Solution()

                testcase_spec = spec_from_file_location("module.name", f"{problem_path}/testcase.py")
                testcase = module_from_spec(testcase_spec)
                testcase_spec.loader.exec_module(testcase)
                testcase_obj = testcase.Testcase()

                for test in testcase_obj.get_testcases():
                    with self.subTest(f"testcase: {test}", testcase=test):
                        i, o = test
                        result = solution_obj.solve(test_input=i)
                        if o is not None:
                            self.assertIsNotNone(result, f"problem: {q}, input = {i}, No solution")
                        try:
                            if o and isinstance(o, list):
                                if isinstance(o[0], float):
                                    for v1, v2 in zip(o, result):
                                        self.assertAlmostEqual(v1, v2, msg=f"problem: {q}, input = {i}", delta=0.00001)
                                elif all(x is not None for x in o) and isinstance(o[0], list) and not any(
                                        None in x for x in o):
                                    self.assertListEqual(sorted(sorted(item) for item in o),
                                                         sorted(sorted(item) for item in result),
                                                         msg=f"problem: {q}, input = {i}")
                                else:
                                    if None not in o and not (isinstance(o[0], list) and any(None in x for x in o)):
                                        self.assertListEqual(sorted(o), sorted(result),
                                                             msg=f"problem: {q}, input = {i}")
                                    else:
                                        self.assertListEqual(o, result, msg=f"problem: {q}, input = {i}")
                            else:
                                if isinstance(o, float):
                                    self.assertAlmostEqual(o, result, msg=f"problem: {q}, input = {i}", delta=0.00001)
                                elif isinstance(o, set) and result and not isinstance(result, set):
                                    self.assertIn(result, o, msg=f"problem: {q}, input = {i}")
                                else:
                                    self.assertEqual(o, result, msg=f"problem: {q}, input = {i}")
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
                                        print(f"Meet expect output in {idx + 2} loop: {result}")
                                        break
                                    except AssertionError as _:
                                        result = solution_obj.solve(test_input=i)
                                if isinstance(o, list):
                                    self.assertListEqual(o, result,
                                                         msg=f"problem: {q}, input = {i},"
                                                             f" Random case not happened in {loop_times + 2} times!")
                                else:
                                    self.assertEqual(o, result,
                                                     msg=f"problem: {q}, input = {i},"
                                                         f" Random case not happened in {loop_times + 2} times!")
                            else:
                                raise ae


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
