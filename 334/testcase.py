from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=True))
        self.testcases.append(case(Input=[5, 4, 3, 2, 1], Output=False))
        self.testcases.append(case(Input=[2, 1, 5, 0, 4, 6], Output=True))
        self.testcases.append(case(Input=[10, 20, 0, 4, 3, 2, 7], Output=True))

    def get_testcases(self):
        return self.testcases
