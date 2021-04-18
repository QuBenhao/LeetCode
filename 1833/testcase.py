from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 2, 4, 1], 7), Output=4))
        self.testcases.append(case(Input=([10, 6, 8, 7, 7, 8], 5), Output=0))
        self.testcases.append(case(Input=([1, 6, 3, 1, 2, 5], 20), Output=6))

    def get_testcases(self):
        return self.testcases
