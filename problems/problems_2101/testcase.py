from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 3], [6, 1, 4]], Output=2))
		self.testcases.append(case(Input=[[1, 1, 5], [10, 10, 5]], Output=1))
		self.testcases.append(case(Input=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], Output=5))

	def get_testcases(self):
		return self.testcases
