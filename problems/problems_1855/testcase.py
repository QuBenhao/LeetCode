from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]), Output=2))
        self.testcases.append(case(Input=([2, 2, 2], [10, 10, 1]), Output=1))
        self.testcases.append(case(Input=([30, 29, 19, 5], [25, 25, 25, 25, 25]), Output=2))
        self.testcases.append(case(Input=([5, 4], [3, 2]), Output=0))

    def get_testcases(self):
        return self.testcases
