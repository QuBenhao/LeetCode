from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 9, 20, None, None, 15, 7], Output=True))
        self.testcases.append(case(Input=[1, 2, 2, 3, 3, None, None, 4, 4], Output=False))
        self.testcases.append(case(Input=[1, 2, 2, 3, None, None, 3, 4, None, None, 4], Output=False))
        self.testcases.append(case(Input=[1,2,3,4,5,6,None,8], Output=True))

    def get_testcases(self):
        return self.testcases
