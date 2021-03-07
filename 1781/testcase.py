from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aabcb", Output=5))
        self.testcases.append(case(Input="aabcbaa", Output=17))

    def get_testcases(self):
        return self.testcases
