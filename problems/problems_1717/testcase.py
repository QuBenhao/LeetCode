from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("cdbcbbaaabab", 4, 5), Output=19))
        self.testcases.append(case(Input=("aabbaaxybbaabb", 5, 4), Output=20))

    def get_testcases(self):
        return self.testcases
