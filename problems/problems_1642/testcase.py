from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([4, 2, 7, 6, 9, 14, 12], 5, 1), Output=4))
        self.testcases.append(case(Input=([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), Output=7))
        self.testcases.append(case(Input=([14, 3, 19, 3], 17, 0), Output=3))

    def get_testcases(self):
        return self.testcases
