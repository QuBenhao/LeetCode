from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abc", "pqr"), Output="apbqcr"))
        self.testcases.append(case(Input=("ab", "pqrs"), Output="apbqrs"))
        self.testcases.append(case(Input=("abcd", "pq"), Output="apbqcd"))

    def get_testcases(self):
        return self.testcases
