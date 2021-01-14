from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 1, 4, 2, 3], 5), Output=2))
        self.testcases.append(case(Input=([5, 6, 7, 8, 9], 4), Output=-1))
        self.testcases.append(case(Input=([3, 2, 20, 1, 1, 3], 10), Output=5))
        self.testcases.append(case(Input=(
        [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365),
                                   Output=16))

    def get_testcases(self):
        return self.testcases
