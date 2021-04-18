from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3], [6, 5]), Output=0))
        self.testcases.append(case(Input=([12], [4]), Output=4))

    def get_testcases(self):
        return self.testcases
