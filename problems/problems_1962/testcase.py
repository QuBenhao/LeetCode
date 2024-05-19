from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, 4, 9], 2), Output=12))
        self.testcases.append(case(Input=([4, 3, 6, 7], 3), Output=12))

    def get_testcases(self):
        return self.testcases
