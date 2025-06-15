from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-1, -9, 2, 3, -2, -3, 1], 1], Output=81))
		self.testcases.append(case(Input=[[1, 3, -5, 5, 6, -4], 3], Output=20))
		self.testcases.append(case(Input=[[2, -1, 2, -6, 5, 2, -5, 7], 2], Output=35))

	def get_testcases(self):
		return self.testcases
