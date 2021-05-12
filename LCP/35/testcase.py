from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=([[1, 3, 3], [3, 2, 1], [2, 1, 3], [0, 1, 4], [3, 0, 5]], 6, 1, 0, [2, 10, 4, 1]), Output=43))
        self.testcases.append(
            case(Input=([[0, 4, 2], [4, 3, 5], [3, 0, 5], [0, 1, 5], [3, 2, 4], [1, 2, 8]], 8, 0, 2, [4, 1, 1, 3, 2]),
                 Output=38))
        self.testcases.append(case(Input=(
        [[3, 6, 9], [0, 7, 24], [5, 3, 27], [7, 6, 1], [1, 2, 41], [3, 6, 28], [2, 3, 30], [5, 0, 41], [0, 3, 13],
         [6, 4, 4], [3, 5, 20], [0, 5, 22], [0, 1, 6], [7, 5, 11], [5, 6, 17], [0, 6, 22], [1, 6, 32], [2, 4, 25],
         [0, 7, 34], [0, 4, 36], [3, 0, 25]], 43, 4, 3, [34, 15, 30, 64, 67, 11, 33, 98]), Output=578))

    def get_testcases(self):
        return self.testcases
