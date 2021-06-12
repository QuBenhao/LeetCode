from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([4, 3, 2, 5, 6, 7, 2, 5, 5], 9), Output="7772"))
        self.testcases.append(case(Input=([7, 6, 5, 5, 5, 6, 8, 7, 8], 12), Output="85"))
        self.testcases.append(case(Input=([2, 4, 6, 2, 4, 6, 4, 4, 4], 5), Output="0"))
        self.testcases.append(case(Input=([6, 10, 15, 40, 40, 40, 40, 40, 40], 47), Output="32211"))
        self.testcases.append(case(Input=([5, 6, 7, 3, 4, 6, 7, 4, 8], 29), Output="884444444"))

    def get_testcases(self):
        return self.testcases
