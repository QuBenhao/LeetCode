from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 5], 11], Output=3))
        self.testcases.append(case(Input=[[2], 3], Output=-1))
        self.testcases.append(case(Input=[[1], 0], Output=0))
        self.testcases.append(case(Input=[[186, 419, 83, 408], 6249], Output=20))

    def get_testcases(self):
        return self.testcases
