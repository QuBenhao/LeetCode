from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=3, Output="III"))
        self.testcases.append(case(Input=4, Output="IV"))
        self.testcases.append(case(Input=9, Output="IX"))
        self.testcases.append(case(Input=58, Output="LVIII"))
        self.testcases.append(case(Input=1994, Output="MCMXCIV"))

    def get_testcases(self):
        return self.testcases
