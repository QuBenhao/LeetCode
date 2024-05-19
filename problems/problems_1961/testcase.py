from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("iloveleetcode", ["i", "love", "leetcode", "apples"]), Output=True))
        self.testcases.append(case(Input=("iloveleetcode", ["apples", "i", "love", "leetcode"]), Output=False))
        self.testcases.append(case(Input=("a", ["aa", "aaaa", "banana"]), Output=False))
        self.testcases.append(case(Input=("z", ["z"]), Output=True))

    def get_testcases(self):
        return self.testcases
