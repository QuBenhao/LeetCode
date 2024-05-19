from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("cabaa", "bcaaa"), Output="cbcabaaaaa"))
        self.testcases.append(case(Input=("abcabc", "abdcaba"), Output="abdcabcabcaba"))

    def get_testcases(self):
        return self.testcases
