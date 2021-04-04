from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("Hello how are you Contestant", 4), Output="Hello how are you"))
        self.testcases.append(case(Input=("What is the solution to this problem", 4), Output="What is the solution"))
        self.testcases.append(case(Input=("chopper is not a tanuki", 5), Output="chopper is not a tanuki"))

    def get_testcases(self):
        return self.testcases
