from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 4, 4, 1], [3, 7, 6, 4, 2]], Output=8))
		self.testcases.append(case(Input=[[0, 1, 2], [1, 1, 1]], Output=2))

	def get_testcases(self):
		return self.testcases
