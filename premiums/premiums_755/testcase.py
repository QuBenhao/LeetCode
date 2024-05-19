from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 1, 2, 1, 2, 2], 4, 3], Output=[2, 2, 2, 3, 2, 2, 2]))
		self.testcases.append(case(Input=[[1, 2, 3, 4], 2, 2], Output=[2, 3, 3, 4]))
		self.testcases.append(case(Input=[[3, 1, 3], 5, 1], Output=[4, 4, 4]))

	def get_testcases(self):
		return self.testcases
