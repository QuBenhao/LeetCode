from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 10, 5, 7], Output=True))
        self.testcases.append(case(Input=[2, 3, 1, 2], Output=False))
        self.testcases.append(case(Input=[1, 1, 1], Output=False))
        self.testcases.append(case(Input=[1, 2, 3], Output=True))

    def get_testcases(self):
        return self.testcases
