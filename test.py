import unittest
from importlib.machinery import SourceFileLoader

# Question ID that wants to test, modify here as passing arguments
QUESTION = 1743
SOLUTION = SourceFileLoader("module.name", f"./{QUESTION}/solution.py").load_module().Solution()
TESTCASE = SourceFileLoader("module.name", f"./{QUESTION}/testcase.py").load_module().Testcase()


class Test(unittest.TestCase):
    def test(self):
        for testcase in TESTCASE.get_testcases():
            i, o = testcase
            result = SOLUTION.solve(test_input=i)
            try:
                self.assertEqual(result, o, msg=f"input = {i}")
            except AssertionError:
                try:
                    self.assertIn(result, o, msg=f"input = {i}")
                except AssertionError:
                    self.assertAlmostEqual(result, o, msg=f"input = {i}", delta=0.00001)


if __name__ == '__main__':
    unittest.main()
