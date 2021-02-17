from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 8, 6, 2, 5, 4, 8, 3, 7], Output=49))
        self.testcases.append(case(Input=[1, 1], Output=1))
        self.testcases.append(case(Input=[4, 3, 2, 1, 4], Output=16))
        self.testcases.append(case(Input=[1, 2, 1], Output=2))

    def get_testcases(self):
        return self.testcases
