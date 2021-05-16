from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 4, 2], Output=6))
        self.testcases.append(case(Input=[2, 2, 3, 3, 3, 4], Output=9))
        self.testcases.append(case(Input=[1], Output=1))
        self.testcases.append(case(Input=[1, 3], Output=4))
        self.testcases.append(case(Input=[1, 1, 1, 2, 4, 5, 5, 5, 6], Output=18))

    def get_testcases(self):
        return self.testcases
