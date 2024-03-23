from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=[['ThroneInheritance', 'birth', 'birth', 'birth', 'birth', 'birth', 'birth', 'getInheritanceOrder',
                    'death', 'getInheritanceOrder'], [['king'], ['king', 'andy'], ['king', 'bob'],
                                                      ['king', 'catherine'], ['andy', 'matthew'], ['bob', 'alex'],
                                                      ['bob', 'asha'], [None], ['bob'], [None]]],
            Output=[None, None, None, None, None, None, None,
                    ['king', 'andy', 'matthew', 'bob', 'alex', 'asha', 'catherine'], None,
                    ['king', 'andy', 'matthew', 'alex', 'asha', 'catherine']]))

    def get_testcases(self):
        return self.testcases
