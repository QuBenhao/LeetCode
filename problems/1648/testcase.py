from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 5], 4), Output=14))
        self.testcases.append(case(Input=([3, 5], 6), Output=19))
        self.testcases.append(case(Input=([2, 8, 4, 10, 6], 20), Output=110))
        self.testcases.append(case(Input=([1000000000], 1000000000), Output=21))

    def get_testcases(self):
        return self.testcases
