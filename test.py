import os.path
import sys
import unittest
from importlib.util import spec_from_file_location, module_from_spec

# Question ID that wants to test, modify here as passing arguments
QUESTION = "2549"
# QUESTION = "Interview/10_02"
# QUESTION = "LCP/07"
# QUESTION = "剑指Offer/52"


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(os.path.exists(f"problems/{QUESTION}"), msg="Please set up the problem env first!")

        solution_spec = spec_from_file_location("module.name", f"./problems/{QUESTION}/solution.py")
        solution = module_from_spec(solution_spec)
        solution_spec.loader.exec_module(solution)
        solution_obj = solution.Solution()

        testcase_spec = spec_from_file_location("module.name", f"./problems/{QUESTION}/testcase.py")
        testcase = module_from_spec(testcase_spec)
        testcase_spec.loader.exec_module(testcase)
        testcase_obj = testcase.Testcase()

        for test in testcase_obj.get_testcases():
            i, o = test
            result = solution_obj.solve(test_input=i)
            try:
                if o and isinstance(o, list) and (None not in o and (isinstance(o[0], list) and not any(None in x for x in o))):
                    self.assertListEqual(sorted(o), sorted(result), msg=f"input = {i}")
                else:
                    self.assertEqual(o, result, msg=f"input = {i}")
            except AssertionError:
                try:
                    self.assertAlmostEqual(o, result, msg=f"input = {i}", delta=0.00001)
                except:
                    self.assertIn(result, o, msg=f"input = {i}")


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
