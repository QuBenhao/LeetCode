from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 2, 0, 2], Output=[13, 4]))
        self.testcases.append(case(Input=[0, 0, 3], Output=[3, 1]))
        self.testcases.append(case(Input=[1, 5, 6, 6, 5, 7, 5, 5, 4, 7], Output=[6859367,5746249]))

    def get_testcases(self):
        return self.testcases
