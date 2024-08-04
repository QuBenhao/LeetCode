from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[5, 1, 4, None, None, 3, 6], Output=False))
        self.testcases.append(case(Input=[2, 1, 3], Output=True))
        self.testcases.append(case(Input=[5, 4, 6, None, None, 3, 7], Output=False))
        self.testcases.append(case(Input=[1, 1], Output=False))
        self.testcases.append(case(Input=[2147483647], Output=True))

    def get_testcases(self):
        return self.testcases
