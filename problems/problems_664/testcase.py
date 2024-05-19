from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aaabbb", Output=2))
        self.testcases.append(case(Input="aba",Output=2))
        self.testcases.append(case(Input="baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa", Output=19))

    def get_testcases(self):
        return self.testcases
