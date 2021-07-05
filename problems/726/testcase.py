from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="H2O", Output="H2O"))
        self.testcases.append(case(Input="Mg(OH)2", Output="H2MgO2"))
        self.testcases.append(case(Input="K4(ON(SO3)2)2", Output="K4N2O14S4"))
        self.testcases.append(case(Input="Be32", Output="Be32"))

    def get_testcases(self):
        return self.testcases
