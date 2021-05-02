from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("5489355142", 4), Output=2))
        self.testcases.append(case(Input=("11112", 4), Output=4))
        self.testcases.append(case(Input=("00123", 1), Output=1))

    def get_testcases(self):
        return self.testcases
