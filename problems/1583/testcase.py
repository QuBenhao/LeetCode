from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]), Output=2))
        self.testcases.append(case(Input=(2, [[1], [0]], [[1, 0]]), Output=0))
        self.testcases.append(case(Input=(4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]]), Output=4))
        self.testcases.append(case(Input=(
        6, [[1, 4, 3, 2, 5], [0, 5, 4, 3, 2], [3, 0, 1, 5, 4], [2, 1, 4, 0, 5], [2, 1, 0, 3, 5], [3, 4, 2, 0, 1]],
        [[3, 1], [2, 0], [5, 4]]), Output=5))

    def get_testcases(self):
        return self.testcases
