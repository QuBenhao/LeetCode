from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"], [[1], [0, 1], [0, 2], [0], [0], [0], [0]]),
                                   Output=[None, None, None, 1, -1, -1, True]))
        self.testcases.append(case(Input=(["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"],
                                          [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]),
                                   Output=[None, None, None, None, 2, 1, -1, -1]))

    def get_testcases(self):
        return self.testcases
