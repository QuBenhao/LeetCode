from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 4, 5, 1, 2], Output=True))
        self.testcases.append(case(Input=[2, 1, 3, 4], Output=False))
        self.testcases.append(case(Input=[1, 2, 3], Output=True))
        self.testcases.append(case(Input=[1, 1, 1], Output=True))
        self.testcases.append(case(Input=[2, 1], Output=True))

    def get_testcases(self):
        return self.testcases
