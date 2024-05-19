from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(1, 1), Output=3))
        self.testcases.append(case(Input=(1, 2), Output=6))
        self.testcases.append(case(Input=(5, 5), Output=580986))
        self.testcases.append(case(Input=(2, 1), Output=6))

    def get_testcases(self):
        return self.testcases
