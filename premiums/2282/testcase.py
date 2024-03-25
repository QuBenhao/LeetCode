from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 1, 4, 2, 5]], Output=[[2, 1, 2, 1, 0]]))
		self.testcases.append(case(Input=[[5, 1], [3, 1], [4, 1]], Output=[[3, 1], [2, 1], [1, 0]]))

	def get_testcases(self):
		return self.testcases
