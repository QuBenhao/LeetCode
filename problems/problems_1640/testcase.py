from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([85], [[85]]), Output=True))
        self.testcases.append(case(Input=([15, 88], [[88], [15]]), Output=True))
        self.testcases.append(case(Input=([49, 18, 16], [[16, 18, 49]]), Output=False))
        self.testcases.append(case(Input=([91, 4, 64, 78], [[78], [4, 64], [91]]), Output=True))
        self.testcases.append(case(Input=([1, 3, 5, 7], [[2, 4, 6, 8]]), Output=False))

    def get_testcases(self):
        return self.testcases
