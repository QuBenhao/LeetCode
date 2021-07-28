import itertools
from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2),
                 Output=[list(i) for i in itertools.permutations([1, 7, 4])]))
        self.testcases.append(case(Input=([1], 1, 3), Output=[]))
        self.testcases.append(
            case(Input=([0, 1, None, 3, 2, 6, None, 5, 4], 3, 1),
                 Output=[list(i) for i in itertools.permutations([1, 6])]))
        self.testcases.append(
            case(Input=([0, None, 1, None, 2, None, 3, 4], 2, 2),
                 Output=[list(i) for i in itertools.permutations([0, 4])]))
        self.testcases.append(case(Input=([0, 1, None, 3, 2], 2, 1), Output=[1]))

    def get_testcases(self):
        return self.testcases
