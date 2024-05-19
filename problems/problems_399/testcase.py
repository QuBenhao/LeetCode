from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
            Output=[6.00000, 0.50000, -1.00000, 1.00000, -1.00000]))
        self.testcases.append(case(Input=(
            [["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
            Output=[3.75000, 0.40000, 5.00000, 0.20000]))
        self.testcases.append(case(Input=([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]),
                                   Output=[0.50000, 2.00000, -1.00000, -1.00000]))
        self.testcases.append(case(Input=([
            [["a", "b"], ["a", "c"], ["a", "d"], ["a", "e"], ["a", "f"], ["a", "g"], ["a", "h"], ["a", "i"], ["a", "j"],
             ["a", "k"], ["a", "l"], ["a", "aa"], ["a", "aaa"], ["a", "aaaa"], ["a", "aaaaa"], ["a", "bb"],
             ["a", "bbb"], ["a", "ff"]],
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 5.0],
            [["d", "f"], ["e", "g"], ["e", "k"], ["h", "a"], ["aaa", "k"], ["aaa", "i"], ["aa", "e"], ["aaa", "aa"],
             ["aaa", "ff"], ["bbb", "bb"], ["bb", "h"], ["bb", "i"], ["bb", "k"], ["aaa", "k"], ["k", "l"], ["x", "k"],
             ["l", "ll"]]]), Output=[1.66667, 1.50000, 2.50000, 0.14286, 10.00000, 8.00000, 4.00000, 1.00000, 5.00000,
                                     0.33333, 7.00000, 8.00000, 10.00000, 10.00000, 1.10000, -1.00000, -1.00000]))

    def get_testcases(self):
        return self.testcases
