from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(3, 2), Output=4))
        self.testcases.append(case(Input=(2, 4), Output=2))
        self.testcases.append(case(Input=(4, 2), Output=8))
        self.testcases.append(case(Input=(4, 3), Output=9))
        self.testcases.append(case(Input=(10, 10), Output=2188))
        self.testcases.append(case(Input=(10, 3), Output=1682))

    def get_testcases(self):
        return self.testcases
