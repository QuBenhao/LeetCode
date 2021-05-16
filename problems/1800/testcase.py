from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[10, 20, 30, 5, 10, 50], Output=65))
        self.testcases.append(case(Input=[10, 20, 30, 40, 50], Output=150))
        self.testcases.append(case(Input=[12, 17, 15, 13, 10, 11, 12], Output=33))
        self.testcases.append(case(Input=[100, 10, 1], Output=100))

    def get_testcases(self):
        return self.testcases
