from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 5, 6, 0, 0, 1, 2], 0), Output=True))
        self.testcases.append(case(Input=([2, 5, 6, 0, 0, 1, 2], 3), Output=False))
        self.testcases.append(case(Input=([2, 2, 2, 0, 2, 2], 0), Output=True))
        self.testcases.append(case(Input=([4,5,6,7,0,1,2],0),Output=True))
        self.testcases.append(case(Input=[[1,0,1,1,1],0], Output=True))
        self.testcases.append(case(Input=[[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2], Output=True))
        self.testcases.append(case(Input=[[1],0], Output=False))

    def get_testcases(self):
        return self.testcases
