from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, -2, 5], [3, 0, -6]], Output=18))
		self.testcases.append(case(Input=[[3, -2], [2, -6, 7]], Output=21))
		self.testcases.append(case(Input=[[-1, -1], [1, 1]], Output=-1))
		self.testcases.append(case(Input=[[-5,-1,-2],[3,3,5,5]], Output=-3))

	def get_testcases(self):
		return self.testcases
