from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[6, 10, 3], Output=5))
        self.testcases.append(case(Input=[5, 15, 40, 5, 6], Output=7))

    def get_testcases(self):
        return self.testcases
