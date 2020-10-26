from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append((([2,3,5,1,3],3),[True,True,True,False,True]))
        self.testcases.append((([4,2,1,1,2],1),[True,False,False,False,False]))
        self.testcases.append((([12,1,12],10),[True,False,True]))

    def get_testcases(self):
        return self.testcases
