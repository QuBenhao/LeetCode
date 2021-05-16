from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, 2), Output=[3, 1, 0]))
        self.testcases.append(case(Input=(8, 11), Output=[6, 0, 4]))

    def get_testcases(self):
        return self.testcases
