from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=[["SAVE20", "", "PHARMA5", "SAVE@20"], ["restaurant", "grocery", "pharmacy", "restaurant"],
                   [True, True, True, True]], Output=['PHARMA5', 'SAVE20']))
        self.testcases.append(case(
            Input=[["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"], ["grocery", "electronics", "invalid"],
                   [False, True, True]], Output=['ELECTRONICS_50']))
		self.testcases.append(case(Input=[["1OFw","0MvB"],["electronics","pharmacy"],[True,True]], Output=["1OFw","0MvB"]))

    def get_testcases(self):
        return self.testcases
