from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        from itertools import permutations
        self.testcases = []
        self.testcases.append(
            case(Input="a1b2", Output=[list(x) for x in permutations(["a1b2", "a1B2", "A1b2", "A1B2"])]))
        self.testcases.append(case(Input="3z4", Output=[list(x) for x in permutations(["3z4", "3Z4"])]))
        self.testcases.append(case(Input="12345", Output=[list(x) for x in permutations(["12345"])]))
        self.testcases.append(case(Input="0", Output=[list(x) for x in permutations(["0"])]))

    def get_testcases(self):
        return self.testcases
