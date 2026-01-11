from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1], [3, 4], [-1, 0]], Output=7))
		self.testcases.append(case(Input=[[3, 2], [-2, 2]], Output=5))

	def get_testcases(self):
		return self.testcases
