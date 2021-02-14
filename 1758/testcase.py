from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="0100", Output=1))
        self.testcases.append(case(Input="10", Output=0))
        self.testcases.append(case(Input="1111", Output=2))

    def get_testcases(self):
        return self.testcases
