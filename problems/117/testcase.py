from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, None, 7], Output=[1, None, 2, 3, None, 4, 5, 7, None]))
        self.testcases.append(case(Input=[-9, -3, 2, None, 4, 4, 0, -6, None, -5],
                                   Output=[-9, None, -3, 2, None, 4, 4, 0, None, -6, -5, None]))

    def get_testcases(self):
        return self.testcases
