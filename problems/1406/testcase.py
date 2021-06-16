from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 7], Output="Bob"))
        self.testcases.append(case(Input=[1, 2, 3, -9], Output="Alice"))
        self.testcases.append(case(Input=[1, 2, 3, 6], Output="Tie"))
        self.testcases.append(case(Input=[1, 2, 3, -1, -2, -3, 7], Output="Alice"))
        self.testcases.append(case(Input=[-1, -2, -3], Output="Tie"))

    def get_testcases(self):
        return self.testcases
