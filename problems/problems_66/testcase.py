from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3], Output=[1, 2, 4]))
        self.testcases.append(case(Input=[4, 3, 2, 1], Output=[4, 3, 2, 2]))
        self.testcases.append(case(Input=[0], Output=[1]))
        self.testcases.append(case(Input=[9, 9, 9, 9], Output=[1, 0, 0, 0, 0]))

    def get_testcases(self):
        return self.testcases
