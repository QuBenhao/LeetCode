from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=int('0b0000000000000000000000000001011', 2), Output=3))
        self.testcases.append(case(Input=int('0b00000000000000000000000010000000', 2), Output=1))
        self.testcases.append(case(Input=int('0b11111111111111111111111111111101', 2), Output=31))

    def get_testcases(self):
        return self.testcases
