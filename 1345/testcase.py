from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404], Output=3))
        self.testcases.append(case(Input=[7], Output=0))
        self.testcases.append(case(Input=[7, 6, 9, 6, 9, 6, 9, 7], Output=1))
        self.testcases.append(case(Input=[6, 1, 9], Output=2))
        self.testcases.append(case(Input=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13], Output=3))

    def get_testcases(self):
        return self.testcases
