from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="abbxxxxzzy", Output=[[3, 6]]))
        self.testcases.append(case(Input="abc", Output=[]))
        self.testcases.append(case(Input="abcdddeeeeaabbbcd", Output=[[3, 5], [6, 9], [12, 14]]))
        self.testcases.append(case(Input="aba", Output=[]))
        self.testcases.append(case(Input="aaa", Output=[[0, 2]]))

    def get_testcases(self):
        return self.testcases
