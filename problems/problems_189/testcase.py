from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4, 5, 6, 7], 3), Output=[5, 6, 7, 1, 2, 3, 4]))
        self.testcases.append(case(Input=([-1, -100, 3, 99], 2), Output=[3, 99, -1, -100]))
        self.testcases.append(case(Input=([-1], 2), Output=[-1]))
        self.testcases.append(case(Input=([1, 2, 3], 4), Output=[3, 1, 2]))
        self.testcases.append(case(Input=[[1],0], Output=[1]))

    def get_testcases(self):
        return self.testcases
