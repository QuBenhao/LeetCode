from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append((([2,5,1,3,4,7],3),[2,3,5,4,1,7]))
        self.testcases.append((([1,2,3,4,4,3,2,1],4),[1,4,2,3,3,2,4,1]))
        self.testcases.append((([1,1,2,2],2),[1,2,1,2]))

    def get_testcases(self):
        return self.testcases
