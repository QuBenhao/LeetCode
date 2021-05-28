from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2], [2, 4], [4, 8]], Output=8))
        self.testcases.append(case(Input=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], Output=32))
        self.testcases.append(case(Input=[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], Output=27))

    def get_testcases(self):
        return self.testcases
