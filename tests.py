import os.path
import sys
import unittest
from importlib.util import spec_from_file_location, module_from_spec
import constants
from dotenv import load_dotenv
from utils import get_default_folder

# Question ID that wants to test, modify here as passing arguments
QUESTIONS = ['191', '427']


class Test(unittest.TestCase):
    def test(self):
        load_dotenv()
        problem_folder = os.getenv(constants.PROBLEM_FOLDER, get_default_folder())

        for q in QUESTIONS:
            print(f"Testing problem: {q}")

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
                i, o = test
                result = solution_obj.solve(test_input=i)
                try:
                    if o and isinstance(o, list) and isinstance(o[0], float):
                        for v1, v2 in zip(o, result):
                            self.assertAlmostEqual(v1, v2, msg=f"problem: {q}, input = {i}", delta=0.00001)
                    elif o and isinstance(o, list) and (None not in o and (isinstance(o[0], list) and not any(None in x for x in o))):
                        self.assertListEqual(sorted(o), sorted(result), msg=f"problem: {q}, input = {i}")
                    else:
                        self.assertEqual(o, result, msg=f"problem: {q}, input = {i}")
                except AssertionError:
                    try:
                        self.assertAlmostEqual(o, result, msg=f"problem: {q}, input = {i}", delta=0.00001)
                    except:
                        self.assertIn(result, o, msg=f"problem: {q}, input = {i}")


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
