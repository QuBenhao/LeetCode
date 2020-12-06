from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=1, Output=1))
        self.testcases.append(case(Input=3, Output=27))
        self.testcases.append(case(Input=12, Output=505379714))

    def get_testcases(self):
        return self.testcases
