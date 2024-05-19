from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(1,  2), Output=2))
        self.testcases.append(case(Input=(2,  6), Output=3))
        self.testcases.append(case(Input=(3,  14), Output=4))

    def get_testcases(self):
        return self.testcases
