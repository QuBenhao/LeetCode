from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=["a", "a", "b", "b", "c", "c", "c"], Output=["a", "2", "b", "2", "c", "3"]))
        self.testcases.append(case(Input=["a"], Output=["a"]))
        self.testcases.append(
            case(Input=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], Output=["a", 'b', '1', '2']))
        self.testcases.append(case(Input=["a", "a", "a", "b", "b", "a", "a"], Output=["a", '3', 'b', '2', 'a', '2']))

    def get_testcases(self):
        return self.testcases
