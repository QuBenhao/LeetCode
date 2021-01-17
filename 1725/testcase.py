from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[5, 8], [3, 9], [5, 12], [16, 5]], Output=3))
        self.testcases.append(case(Input=[[2, 3], [3, 7], [4, 3], [3, 7]], Output=3))

    def get_testcases(self):
        return self.testcases
