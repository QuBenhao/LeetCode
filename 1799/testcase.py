from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2], Output=1))
        self.testcases.append(case(Input=[3, 4, 6, 8], Output=11))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6], Output=14))

    def get_testcases(self):
        return self.testcases
