from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 10], [5, 15], [10, 2], [4, 4]], Output=12))
		self.testcases.append(case(Input=[[1, 1], [1, 1], [1, 1]], Output=0))

	def get_testcases(self):
		return self.testcases
