from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 3, 1, 3, 1, None, 1], Output=2))
        self.testcases.append(case(Input=[2, 1, 1, 1, 3, None, None, None, None, None, 1], Output=1))
        self.testcases.append(case(Input=[9], Output=1))

    def get_testcases(self):
        return self.testcases
