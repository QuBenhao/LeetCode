from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="1-23-45 6", Output="123-456"))
        self.testcases.append(case(Input="123 4-567", Output="123-45-67"))
        self.testcases.append(case(Input="123 4-5678", Output="123-456-78"))
        self.testcases.append(case(Input="12", Output="12"))
        self.testcases.append(case(Input="--17-5 229 35-39475 ", Output="175-229-353-94-75"))

    def get_testcases(self):
        return self.testcases
