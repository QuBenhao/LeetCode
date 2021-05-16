from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="is2 sentence4 This1 a3", Output="This is a sentence"))
        self.testcases.append(case(Input="Myself2 Me1 I4 and3", Output="Me Myself and I"))

    def get_testcases(self):
        return self.testcases
