from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 5], [3, 4], 2], Output=8))
		self.testcases.append(case(Input=[[-4, -2, 0, 3], [2, 4], 6], Output=0))
		self.testcases.append(case(Input=[[-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3], Output=-6))

	def get_testcases(self):
		return self.testcases
