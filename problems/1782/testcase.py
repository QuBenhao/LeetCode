from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3]), Output=[6, 5]))
        self.testcases.append(
            case(Input=(5, [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]], [1, 2, 3, 4, 5]),
                 Output=[10, 10, 9, 8, 6]))

    def get_testcases(self):
        return self.testcases
