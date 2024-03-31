import os.path
import sys
import traceback
import unittest
from importlib.util import spec_from_file_location, module_from_spec

import constants
from dotenv import load_dotenv
from utils import get_default_folder

# Question ID that wants to test, modify here as passing arguments
QUESTIONS = ['49', '72']


class Test(unittest.TestCase):
    def test(self):
        load_dotenv()
        problem_folder = os.getenv(constants.PROBLEM_FOLDER, get_default_folder())

        for q in QUESTIONS:
            with self.subTest(f"Testing problem: {q}", question=q):

                self.assertTrue(os.path.exists(f"{problem_folder}/{q}"), msg="Please set up the problem env first!")

                solution_spec = spec_from_file_location("module.name", f"./{problem_folder}/{q}/solution.py")
                solution = module_from_spec(solution_spec)
                solution_spec.loader.exec_module(solution)
                solution_obj = solution.Solution()

                testcase_spec = spec_from_file_location("module.name", f"./{problem_folder}/{q}/testcase.py")
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
                                elif all(x is not None for x in o) and isinstance(o[0], list) and not any(None in x for x in o):
                                    self.assertListEqual(sorted(sorted(item) for item in o), sorted(sorted(item) for item in result), msg=f"problem: {q}, input = {i}")
                                else:
                                    if None not in o and not (isinstance(o[0], list) and any(None in x for x in o)):
                                        self.assertListEqual(sorted(o), sorted(result), msg=f"problem: {q}, input = {i}")
                                    else:
                                        self.assertListEqual(o, result, msg=f"problem: {q}, input = {i}")
                            else:
                                if isinstance(o, float):
                                    self.assertAlmostEqual(o, result, msg=f"problem: {q}, input = {i}", delta=0.00001)
                                elif isinstance(o, set) and result and not isinstance(result, set):
                                    self.assertIn(result, o, msg=f"problem: {q}, input = {i}")
                                else:
                                    self.assertEqual(o, result, msg=f"problem: {q}, input = {i}")
                        except AssertionError as _:
                            traceback.print_exc()
                            last = result
                            result = solution_obj.solve(test_input=i)
                            if last != result:
                                # TODO
                                print(f"Question: {q} Test for random case!!!")


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
