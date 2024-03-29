from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="1234", Output=False))
        self.testcases.append(case(Input="050043", Output=True))
        self.testcases.append(case(Input="9080701", Output=False))
        self.testcases.append(case(Input="10009998", Output=True))

    def get_testcases(self):
        return self.testcases
