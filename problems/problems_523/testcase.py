from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([23, 2, 4, 6, 7], 6), Output=True))
        self.testcases.append(case(Input=([23, 2, 6, 4, 7], 6), Output=True))
        self.testcases.append(case(Input=([23, 2, 6, 4, 7], 13), Output=False))
        self.testcases.append(case(Input=([23, 2, 4, 6, 6], 7), Output=True))
        self.testcases.append(case(Input=([5, 0, 0, 0], 3), Output=True))
        self.testcases.append(case(Input=([1, 0], 2), Output=False))
        self.testcases.append(case(Input=([1, 2, 3], 5), Output=True))
        self.testcases.append(case(Input=([2, 4, 3], 6), Output=True))
        self.testcases.append(case(Input=([0, 0, 3], 6), Output=True))
        self.testcases.append(case(Input=([0, 3, 0], 6), Output=False))

    def get_testcases(self):
        return self.testcases
