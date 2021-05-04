from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3), Output=9))
        self.testcases.append(
            case(Input=([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3), Output=11))
        self.testcases.append(
            case(Input=([0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5), Output=5))
        self.testcases.append(
            case(Input=([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3), Output=-1))
        self.testcases.append(case(Input=([0, 0, 0, 1], [[1, 5], [4, 1], [1, 3], [4, 4]], 4, 2, 4), Output=12))
        self.testcases.append(case(Input=([0, 1, 0, 0, 1, 2, 0, 0, 2, 1],
                                          [[4, 5, 2, 6], [8, 3, 2, 9], [6, 7, 3, 1], [10, 10, 2, 7], [6, 5, 2, 4],
                                           [4, 4, 3, 9], [9, 8, 3, 5], [7, 9, 10, 3], [8, 5, 9, 10], [10, 7, 4, 6]], 10,
                                          4, 6), Output=24))
        self.testcases.append(
            case(Input=([0, 0, 0, 3], [[2, 2, 5], [1, 5, 5], [5, 1, 2], [5, 2, 5]], 4, 3, 3), Output=4))

    def get_testcases(self):
        return self.testcases
