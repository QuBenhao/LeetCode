from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 9, 4], [6, 6, 8], [2, 1, 1]], Output=4))
		self.testcases.append(case(Input=[[3, 4, 5], [3, 2, 6], [2, 2, 1]], Output=4))
		self.testcases.append(case(Input=[[1]], Output=1))

	def get_testcases(self):
		return self.testcases
