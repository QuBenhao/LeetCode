from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aeiaaioaaaaeiiiiouuuooaauuaeiu", Output=13))
        self.testcases.append(case(Input="aeeeiiiioooauuuaeiou", Output=5))
        self.testcases.append(case(Input="a", Output=0))

    def get_testcases(self):
        return self.testcases
