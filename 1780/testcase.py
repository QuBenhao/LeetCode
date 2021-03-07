from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=12, Output=True))
        self.testcases.append(case(Input=91, Output=True))
        self.testcases.append(case(Input=21, Output=False))
        self.testcases.append(case(Input=111720, Output=False))

    def get_testcases(self):
        return self.testcases
