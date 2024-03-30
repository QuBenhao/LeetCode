from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 7, 11], [2, 4, 6], 3], Output=[[1, 2], [1, 4], [1, 6]]))
        self.testcases.append(case(Input=[[1, 1, 2], [1, 2, 3], 2], Output=[[1, 1], [1, 1]]))
        self.testcases.append(case(Input=[[1, 2, 4, 5, 6], [3, 5, 7, 9], 3], Output=[[1, 3], [2, 3], [1, 5]]))
        self.testcases.append(case(Input=[[1, 2, 4, 5, 6], [3, 5, 7, 9], 20],
                                   Output=[[1, 3], [2, 3], [1, 5], [2, 5], [4, 3], [1, 7], [5, 3], [2, 7], [4, 5],
                                           [6, 3], [1, 9], [5, 5], [2, 9], [4, 7], [6, 5], [5, 7], [4, 9], [6, 7],
                                           [5, 9], [6, 9]]))

    def get_testcases(self):
        return self.testcases
