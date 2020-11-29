import unittest
from importlib.machinery import SourceFileLoader

# Question ID that wants to test, modify here as passing arguments
QUESTION = 1290
SOLUTION = SourceFileLoader("module.name", f"./{QUESTION}/solution.py").load_module().Solution()
TESTCASE = SourceFileLoader("module.name", f"./{QUESTION}/testcase.py").load_module().Testcase()


class Test(unittest.TestCase):
    def test(self):
        for testcase in TESTCASE.get_testcases():
            i, o = testcase
            self.assertEqual(o, SOLUTION.solve(test_input=i),msg=f"input = {i}")


if __name__ == '__main__':
    unittest.main()
