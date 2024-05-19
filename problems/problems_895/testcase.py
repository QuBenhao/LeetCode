from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
            ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
            [[], [5], [7], [5], [7], [4], [5], [], [], [], []]),
            Output=[None, None, None, None, None, None, None, 5, 7, 5, 4]))
        self.testcases.append(case(Input=(
        ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "push", "pop", "push", "pop", "push",
         "pop", "push", "pop", "pop", "pop", "pop", "pop", "pop"],
        [[], [4], [0], [9], [3], [4], [2], [], [6], [], [1], [], [1], [], [4], [], [], [], [], [], []]),
                                   Output=[None, None, None, None, None, None, None, 4, None, 6, None, 1, None, 1, None,
                                           4, 2, 3, 9, 0, 4]))

    def get_testcases(self):
        return self.testcases
