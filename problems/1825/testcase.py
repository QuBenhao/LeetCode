from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage",
         "addElement", "addElement", "addElement", "calculateMKAverage"],
        [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]),
                                   Output=[None, None, None, -1, None, 3, None, None, None, 5]))

    def get_testcases(self):
        return self.testcases
