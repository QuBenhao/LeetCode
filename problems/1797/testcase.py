from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew",
         "countUnexpiredTokens"], [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]),
                                   Output=[None, None, None, 1, None, None, None, 0]))

    def get_testcases(self):
        return self.testcases
