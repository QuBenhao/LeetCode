from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(1, 2, 3), Output=2))
        self.testcases.append(case(Input=(4, 2, 3), Output=6))
        self.testcases.append(case(Input=(5, 2, 4), Output=10))
        self.testcases.append(case(Input=(3, 4, 6), Output=8))
        self.testcases.append(case(Input=(1000000000, 40000, 40000), Output=999720007))
        self.testcases.append(case(Input=(10, 9, 4), Output=28))
        self.testcases.append(case(Input=(10, 10, 8), Output=50))

    def get_testcases(self):
        return self.testcases
