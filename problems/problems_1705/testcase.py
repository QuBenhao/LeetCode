from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]), Output=7))
        self.testcases.append(case(Input=([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]), Output=5))
        self.testcases.append(case(Input=[[9,10,1,7,0,2,1,4,1,7,0,11,0,11,0,0,9,11,11,2,0,5,5],[3,19,1,14,0,4,1,8,2,7,0,13,0,13,0,0,2,2,13,1,0,3,7]], Output=31))
        self.testcases.append(case(Input=[[2,1,10],[2,10,1]], Output=4))

    def get_testcases(self):
        return self.testcases
