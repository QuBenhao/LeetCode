from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abcacb", "ab", [3, 1, 0]), Output=2))
        self.testcases.append(case(Input=("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]), Output=1))
        self.testcases.append(case(Input=("abcab", "abc", [0, 1, 2, 3, 4]), Output=0))

    def get_testcases(self):
        return self.testcases
