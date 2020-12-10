from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
                                   Output=[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]))
        self.testcases.append(case(Input=[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
                                   Output=[[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]))
        self.testcases.append(case(Input=
                                   [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]],
                                   Output=
                                   [[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [5, 3], [6, 2], [2, 7], [9, 0], [1, 9]]))

    def get_testcases(self):
        return self.testcases
