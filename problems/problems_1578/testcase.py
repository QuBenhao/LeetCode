from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abaac', [1, 2, 3, 4, 5]], Output=3))
		self.testcases.append(case(Input=['abc', [1, 2, 3]], Output=0))
		self.testcases.append(case(Input=['aabaa', [1, 2, 3, 4, 1]], Output=2))
		self.testcases.append(case(Input=["aaabbbabbbb",[3,5,10,7,5,3,5,5,4,8,1]], Output=26))

	def get_testcases(self):
		return self.testcases
