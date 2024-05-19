from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["10", "0001", "111001", "1", "0"], 5, 3), Output=4))
        self.testcases.append(case(Input=(["10", "0", "1"], 1, 1), Output=2))

    def get_testcases(self):
        return self.testcases
