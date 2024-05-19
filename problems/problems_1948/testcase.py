from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=[["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]],
                 Output=[["c"], ["c", "b"], ["a"], ["a", "b"]]))
        self.testcases.append(
            case(Input=[["a", "b"], ["c", "d"], ["c"], ["a"]], Output=[["c"], ["c", "d"], ["a"], ["a", "b"]]))
        self.testcases.append(
            case(Input=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]], Output=[["d"], ["d", "a"]]))
        self.testcases.append(
            case(Input=[["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"]],
                 Output=[]))
        self.testcases.append(case(
            Input=[["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"],
                   ["b", "w"]], Output=[["b"], ["b", "w"], ["b", "z"], ["a"], ["a", "z"]]))

    def get_testcases(self):
        return self.testcases
