from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        # self.testcases.append(case(Input=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
        #                                   [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]],
        #                            Output=4))
        # self.testcases.append(case(Input=[[-1, -1, 2, -1], [14, 2, 12, 3], [4, 9, 1, 11], [-1, 2, 1, 16]], Output=1))
        self.testcases.append(case(
            Input=[[-1, -1, -1, 46, 47, -1, -1, -1], [51, -1, -1, 63, -1, 31, 21, -1], [-1, -1, 26, -1, -1, 38, -1, -1],
                   [-1, -1, 11, -1, 14, 23, 56, 57], [11, -1, -1, -1, 49, 36, -1, 48], [-1, -1, -1, 33, 56, -1, 57, 21],
                   [-1, -1, -1, -1, -1, -1, 2, -1], [-1, -1, -1, 8, 3, -1, 6, 56]], Output=4))

    def get_testcases(self):
        return self.testcases
