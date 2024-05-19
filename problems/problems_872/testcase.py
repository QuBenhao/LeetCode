from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]),
                                   Output=True))
        self.testcases.append(case(Input=([1], [1]), Output=True))
        self.testcases.append(case(Input=([1], [2]), Output=False))
        self.testcases.append(case(Input=([1, 2], [2, 2]), Output=True))
        self.testcases.append(case(Input=([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
                                          [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None,
                                           8, 10]), Output=False))

    def get_testcases(self):
        return self.testcases
