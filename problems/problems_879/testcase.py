from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(5, 3, [2, 2], [2, 3]), Output=2))
        self.testcases.append(case(Input=(10, 5, [2, 3, 5], [6, 7, 8]), Output=7))
        self.testcases.append(case(Input=[64,0,[80, 40],[88, 88]], Output=2))

    def get_testcases(self):
        return self.testcases
