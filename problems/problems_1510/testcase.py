from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=1, Output=True))
        self.testcases.append(case(Input=2, Output=False))
        self.testcases.append(case(Input=4, Output=True))
        self.testcases.append(case(Input=7, Output=False))
        self.testcases.append(case(Input=17, Output=False))

    def get_testcases(self):
        return self.testcases
