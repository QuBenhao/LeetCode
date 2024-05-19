from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abc", "bca"),Output=True))
        self.testcases.append(case(Input=("a","aa"),Output=False))
        self.testcases.append(case(Input=("cabbba","abbccc"),Output=True))
        self.testcases.append(case(Input=("cabbba","aabbss"),Output=False))
        self.testcases.append(case(Input=("uau", "ssx"),Output=False))

    def get_testcases(self):
        return self.testcases
