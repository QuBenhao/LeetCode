from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(5,0),Output=8))
        self.testcases.append(case(Input=(4,3),Output=8))
        self.testcases.append(case(Input=(1,7),Output=7))
        self.testcases.append(case(Input=(10,5),Output=2))


    def get_testcases(self):
        return self.testcases