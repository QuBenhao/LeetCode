from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["TimeMap", "set", "get", "get", "set", "get", "get"],
                                          [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4],
                                           ["foo", 4], ["foo", 5]]),
                                   Output=[None, None, "bar", "bar", None, "bar2", "bar2"]))
        self.testcases.append(case(Input=(["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
                                          [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10],
                                           ["love", 15], ["love", 20], ["love", 25]]),
                                   Output=[None, None, None, "", "high", "high", "low", "low"]))

    def get_testcases(self):
        return self.testcases
