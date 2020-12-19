from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("1.01", "1.001"), Output=0))
        self.testcases.append(case(Input=("1.0", "1.0.0"), Output=0))
        self.testcases.append(case(Input=("0.1", "1.1"), Output=-1))
        self.testcases.append(case(Input=("1.0.1", "1"), Output=1))
        self.testcases.append(case(Input=("7.5.2.4", "7.5.3"), Output=-1))
        self.testcases.append(case(Input=("0.1", "1.0"), Output=-1))
        self.testcases.append(case(Input=("0.1", "0.0.1"), Output=1))

    def get_testcases(self):
        return self.testcases
