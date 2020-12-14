from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[5, 3, 1, 4, 2], Output=6))
        self.testcases.append(case(Input=[7, 90, 5, 1, 100, 10, 10, 2], Output=122))

    def get_testcases(self):
        return self.testcases
