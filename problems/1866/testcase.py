from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(3, 2), Output=3))
        self.testcases.append(case(Input=(5, 5), Output=1))
        self.testcases.append(case(Input=(20, 11), Output=647427950))

    def get_testcases(self):
        return self.testcases
