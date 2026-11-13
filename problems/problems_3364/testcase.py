from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, -2, 1, 4], 2, 3], Output=1))
		self.testcases.append(case(Input=[[-2, 2, -3, 1], 2, 3], Output=-1))
		self.testcases.append(case(Input=[[1, 2, 3, 4], 2, 4], Output=3))

	def get_testcases(self):
		return self.testcases
