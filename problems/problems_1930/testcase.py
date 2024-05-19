from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aabca", Output=3))
        self.testcases.append(case(Input="adc", Output=0))
        self.testcases.append(case(Input="bbcbaba", Output=4))

    def get_testcases(self):
        return self.testcases
