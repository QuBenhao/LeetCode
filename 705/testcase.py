from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=(["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
                        [[], [1], [2], [1], [3], [2], [2], [2], [2]]),
                 Output=[None, None, None, True, False, None, True, None, False]))
        self.testcases.append(case(Input=(
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains", "add", "contains"],
        [[], [1], [2], [1], [3], [2], [2], [2], [2], [1000000], [1000000]]),
                                   Output=[None, None, None, True, False, None, True, None, False, None, True]))

    def get_testcases(self):
        return self.testcases
