from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[6, 2, 3, 4, 5, 5], Output=18))
        self.testcases.append(case(Input=[7, 7, 7, 7, 7, 7, 7], Output=28))
        self.testcases.append(case(Input=[4], Output=0))
        self.testcases.append(case(Input=[6, 1], Output=1))
        self.testcases.append(case(Input=[98, 77, 24, 49, 6, 12, 2, 44, 51, 96], Output=330))

    def get_testcases(self):
        return self.testcases
