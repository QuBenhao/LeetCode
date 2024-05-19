from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], Output=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]))
		self.testcases.append(case(Input=[[1, 1], [2, 1]], Output=[[1, 1], [2, 1]]))
		self.testcases.append(case(Input=[[3, None], [3, 0], [3, None]], Output=[[3, None], [3, 0], [3, None]]))

	def get_testcases(self):
		return self.testcases
