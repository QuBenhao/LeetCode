from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("loveleetcode", "e"), Output=[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]))
        self.testcases.append(case(Input=("aaab", "b"), Output=[3, 2, 1, 0]))

    def get_testcases(self):
        return self.testcases
