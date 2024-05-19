from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, 3), Output=2))
        self.testcases.append(case(Input=(5, 8), Output=2))
        self.testcases.append(case(Input=(3, 10), Output=3))
        self.testcases.append(case(Input=(1024, 1), Output=1023))
        self.testcases.append(case(Input=(1,1000000000), Output=39))
        self.testcases.append(case(Input=(9411921, 9411923), Output=4705961))

    def get_testcases(self):
        return self.testcases
