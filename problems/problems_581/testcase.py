from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2,6,4,8,10,9,15], Output=5))
        self.testcases.append(case(Input=[1, 2, 3, 4], Output=0))
        self.testcases.append(case(Input=[1], Output=0))
        self.testcases.append(case(Input=[2,1], Output=2))
        self.testcases.append(case(Input=[1,3,2,2,2], Output=4))
        self.testcases.append(case(Input=[2,3,3,2,4], Output=3))
        self.testcases.append(case(Input=[1,2,4,5,3], Output=3))

    def get_testcases(self):
        return self.testcases
