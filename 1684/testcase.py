from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("ab", ["ad", "bd", "aaab", "baa", "badab"]), Output=2))
        self.testcases.append(case(Input=("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]), Output=7))
        self.testcases.append(case(Input=("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]), Output=4))

    def get_testcases(self):
        return self.testcases
