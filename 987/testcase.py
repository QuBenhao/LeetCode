from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 9, 20, None, None, 15, 7], Output=[[9], [3, 15], [20], [7]]))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, 7], Output=[[4], [2], [1, 5, 6], [3], [7]]))
        self.testcases.append(case(Input=[0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9],
                                   Output=[[4, 10, 11], [3, 6, 7], [2, 5, 8, 9], [0], [1]]))
        self.testcases.append(case(Input=[0, 5, 1, 9, None, 2, None, None, None, None, 3, 4, 8, 6, None, None, None, 7],
                                   Output=[[9, 7], [5, 6], [0, 2, 4], [1, 3], [8]]))

    def get_testcases(self):
        return self.testcases
