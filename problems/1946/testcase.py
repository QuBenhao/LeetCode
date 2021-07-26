from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]), Output="832"))
        self.testcases.append(case(Input=("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]), Output="934"))
        self.testcases.append(case(Input=("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]), Output="5"))

    def get_testcases(self):
        return self.testcases
