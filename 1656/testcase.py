from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
                                          [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]),
                                   Output=[None, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]))


    def get_testcases(self):
        return self.testcases