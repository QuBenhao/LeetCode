from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([10, 5, 15, 3, 7, None, 18], 7, 15), Output=32))
        self.testcases.append(case(Input=([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10), Output=23))

    def get_testcases(self):
        return self.testcases
