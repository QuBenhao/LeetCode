from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=(["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]),
                 Output=[None, None, None, 1, 1, False]))
        self.testcases.append(case(Input=(
        ["MyQueue", "push", "push", "push", "push", "pop", "push", "pop", "pop", "pop", "pop"],
        [[], [1], [2], [3], [4], [], [5], [], [], [], []]), Output=[None, None, None, None, None, 1, None, 2, 3, 4, 5]))

    def get_testcases(self):
        return self.testcases
