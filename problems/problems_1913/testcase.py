from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[5, 6, 2, 7, 4], Output=34))
        self.testcases.append(case(Input=[4, 2, 5, 9, 7, 4, 8], Output=64))

    def get_testcases(self):
        return self.testcases
