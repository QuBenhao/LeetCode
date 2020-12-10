from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 1], Output=False))
        self.testcases.append(case(Input=[3, 5, 5], Output=False))
        self.testcases.append(case(Input=[0, 3, 2, 1], Output=True))
        self.testcases.append(case(Input=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], Output=False))
        self.testcases.append(case(Input=[4, 3, 2, 1], Output=False))

    def get_testcases(self):
        return self.testcases
