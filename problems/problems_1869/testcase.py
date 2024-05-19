from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="1101", Output=True))
        self.testcases.append(case(Input="111000", Output=False))
        self.testcases.append(case(Input="110100010", Output=False))

    def get_testcases(self):
        return self.testcases
