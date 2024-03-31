from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2], Output=[7, 4, 1]))
		self.testcases.append(case(Input=[[1], 1, 3], Output=[]))

	def get_testcases(self):
		return self.testcases
