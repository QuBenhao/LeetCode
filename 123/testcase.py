from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 3, 5, 0, 0, 3, 1, 4], Output=6))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=4))
        self.testcases.append(case(Input=[7, 6, 4, 3, 1], Output=0))
        self.testcases.append(case(Input=[1], Output=0))
        self.testcases.append(case(Input=[2, 1, 2, 0, 1], Output=2))
        self.testcases.append(case(Input=[6, 1, 3, 2, 4, 7], Output=7))
        self.testcases.append(case(Input=[8, 3, 6, 2, 8, 8, 8, 4, 2, 0, 7, 2, 9, 4, 9], Output=15))
        self.testcases.append(case(Input=[8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6], Output=11))
        self.testcases.append(case(Input=[2,4,1],Output=2))

    def get_testcases(self):
        return self.testcases
