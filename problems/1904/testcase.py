from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("12:01", "12:44"), Output=1))
        self.testcases.append(case(Input=("20:00", "06:00"), Output=40))
        self.testcases.append(case(Input=("00:00", "23:59"), Output=95))
        self.testcases.append(case(Input=("12:01", "12:02"), Output=0))

    def get_testcases(self):
        return self.testcases
