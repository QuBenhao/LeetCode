from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[4, 2, 6, 1, 3], Output=1))
        self.testcases.append(case(Input=[1, 0, 48, None, None, 12, 49], Output=1))
        self.testcases.append(case(Input=[27, None, 34, None, 58, 50, None, 44], Output=6))
        self.testcases.append(case(Input=[90, 69, None, 49, 89, None, 52], Output=1))
        self.testcases.append(case(Input=[1, None, 3, 2], Output=1))

    def get_testcases(self):
        return self.testcases
