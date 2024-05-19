from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("123", 6), Output=["1+2+3", "1*2*3"]))
        self.testcases.append(case(Input=("232", 8), Output=["2+3*2","2*3+2"]))
        self.testcases.append(case(Input=("105", 5), Output=["1*0+5","10-5"]))
        self.testcases.append(case(Input=("00", 0), Output=["0+0", "0-0", "0*0"]))
        self.testcases.append(case(Input=("3456237490", 9191), Output=[]))

    def get_testcases(self):
        return self.testcases
