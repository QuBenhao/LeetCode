from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 3], Output=6))
        self.testcases.append(case(Input=[5, 1, 6], Output=28))
        self.testcases.append(case(Input=[3, 4, 5, 6, 7, 8], Output=480))

    def get_testcases(self):
        return self.testcases
