from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
                                   Output=[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]))
        self.testcases.append(case(Input=[[0, 2, 3], [2, 5, 3]], Output=[[0, 3], [5, 0]]))

    def get_testcases(self):
        return self.testcases
