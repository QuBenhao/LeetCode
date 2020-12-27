from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="book", Output=True))
        self.testcases.append(case(Input="textbook", Output=False))
        self.testcases.append(case(Input="MerryChristmas", Output=False))
        self.testcases.append(case(Input="AbCdEfGh", Output=True))

    def get_testcases(self):
        return self.testcases
