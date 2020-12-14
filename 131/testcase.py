from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aab", Output=[["a", "a", "b"], ["aa", "b"]]))
        self.testcases.append(case(Input="a", Output=[["a"]]))

    def get_testcases(self):
        return self.testcases
