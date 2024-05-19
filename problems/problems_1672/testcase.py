from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 3], [3, 2, 1]], Output=6))
        self.testcases.append(case(Input=[[1, 5], [7, 3], [3, 5]], Output=10))
        self.testcases.append(case(Input=[[2, 8, 7], [7, 1, 3], [1, 9, 5]], Output=17))

    def get_testcases(self):
        return self.testcases
