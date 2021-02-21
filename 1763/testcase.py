from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="YazaAay", Output="aAa"))
        self.testcases.append(case(Input="Bb", Output="Bb"))
        self.testcases.append(case(Input="c", Output=""))
        self.testcases.append(case(Input="dDzeE", Output="dD"))

    def get_testcases(self):
        return self.testcases
