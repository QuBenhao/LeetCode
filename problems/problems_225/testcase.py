from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=(["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []]),
                 Output=[None, None, None, 2, 2, False]))

    def get_testcases(self):
        return self.testcases
