from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="abc", Output=["abc","acb","bac","bca","cab","cba"]))
        self.testcases.append(case(Input="aab", Output=["aab", "aba", "baa"]))

    def get_testcases(self):
        return self.testcases
