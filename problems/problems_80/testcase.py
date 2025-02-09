from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 1, 1, 2, 2, 3], Output=(5, [1, 1, 2, 2, 3])))
        self.testcases.append(case(Input=[0, 0, 1, 1, 1, 1, 2, 3, 3], Output=(7, [0, 0, 1, 1, 2, 3, 3])))
        self.testcases.append(case(Input=[1, 1, 1], Output=(2, [1, 1])))
        self.testcases.append(case(Input=[1, 1, 1, 1], Output=(2, [1, 1])))
        self.testcases.append(case(Input=[1, 1, 1, 2], Output=(3, [1, 1, 2])))
        self.testcases.append(case(Input=[1, 1, 1, 2, 2, 2, 3, 3], Output=(6, [1, 1, 2, 2, 3, 3])))
        self.testcases.append(case(Input=[0, 0, 0, 0, 0], Output=(2, [0, 0])))
        self.testcases.append(case(Input=[1, 2, 2, 2], Output=(3, [1, 2, 2])))
        self.testcases.append(case(Input=[1,1,1,2,2,3], Output=(5, [1,1,2,2,3])))

    def get_testcases(self):
        return self.testcases
