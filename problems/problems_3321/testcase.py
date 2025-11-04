from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 2, 2, 3, 4, 2, 3], 6, 2], Output=[6, 10, 12]))
		self.testcases.append(case(Input=[[3, 8, 7, 8, 7, 5], 2, 2], Output=[11, 15, 15, 15, 12]))

	def get_testcases(self):
		return self.testcases
