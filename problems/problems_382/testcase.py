from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[['Solution', 'getRandom', 'getRandom', 'getRandom', 'getRandom', 'getRandom'],
                                          [[[1, 2, 3]], [], [], [], [], []]], Output=[None, 1, 3, 2, 2, 3]))

    def get_testcases(self):
        return self.testcases
