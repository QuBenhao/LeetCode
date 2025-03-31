from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2], [4, 3], [4, 4], [2, 5]], Output=5))
		self.testcases.append(case(Input=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], Output=7))

	def get_testcases(self):
		return self.testcases
