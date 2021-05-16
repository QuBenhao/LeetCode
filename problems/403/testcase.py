from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[0, 1, 3, 5, 6, 8, 12, 17], Output=True))
        self.testcases.append(case(Input=[0, 1, 2, 3, 4, 8, 9, 11], Output=False))
        self.testcases.append(case(Input=[0, 1, 3, 6, 10, 15, 16, 21], Output=True))
        self.testcases.append(case(Input=[0, 1], Output=True))

    def get_testcases(self):
        return self.testcases
