import os.path
import sys
import unittest
from importlib.machinery import SourceFileLoader

# Question ID that wants to test, modify here as passing arguments
QUESTION = 528
# QUESTION = "Interview/10_02"
# QUESTION = "LCP/07"
# QUESTION = "剑指Offer/52"


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(os.path.exists(f"problems/{QUESTION}"), msg="Please set up the problem env first!")

        solution_obj = SourceFileLoader("module.name", f"./problems/{QUESTION}/solution.py").load_module().Solution()
        testcase_obj = SourceFileLoader("module.name", f"./problems/{QUESTION}/testcase.py").load_module().Testcase()
        for testcase in testcase_obj.get_testcases():
            i, o = testcase
            result = solution_obj.solve(test_input=i)
            try:
                if o and type(o) == list and (None not in o and (type(o[0]) == list and not any(None in x for x in o))):
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
