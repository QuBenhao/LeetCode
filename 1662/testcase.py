from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["ab", "c"], ["a", "bc"]), Output=True))
        self.testcases.append(case(Input=(["a", "cb"], ["ab", "c"]), Output=False))
        self.testcases.append(case(Input=(["abc", "d", "defg"], ["abcddefg"]), Output=True))

    def get_testcases(self):
        return self.testcases
