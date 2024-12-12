from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 3, 5, 6], 5, 2], Output=[8, 4, 6, 5, 6]))
		self.testcases.append(case(Input=[[1, 2], 3, 4], Output=[16, 8]))

	def get_testcases(self):
		return self.testcases
