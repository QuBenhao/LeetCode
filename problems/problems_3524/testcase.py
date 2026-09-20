from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 3], Output=[9, 2, 4]))
		self.testcases.append(case(Input=[[1, 2, 4, 8, 16, 32], 4], Output=[18, 1, 2, 0]))
		self.testcases.append(case(Input=[[1, 1, 2, 1, 1], 2], Output=[9, 6]))

	def get_testcases(self):
		return self.testcases
