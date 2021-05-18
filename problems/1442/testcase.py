from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 3, 1, 6, 7], Output=4))
        self.testcases.append(case(Input=[1, 1, 1, 1, 1], Output=10))
        self.testcases.append(case(Input=[2, 3], Output=0))
        self.testcases.append(case(Input=[1, 3, 5, 7, 9], Output=3))
        self.testcases.append(case(Input=[7, 11, 12, 9, 5, 2, 7, 17, 22], Output=8))

    def get_testcases(self):
        return self.testcases
