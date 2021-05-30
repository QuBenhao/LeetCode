from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, 3, 1, 2), Output=240))
        self.testcases.append(case(Input=(3, 1, 2, 1), Output=260))
        self.testcases.append(case(Input=(2, 2, 4, 0), Output=240))

    def get_testcases(self):
        return self.testcases
