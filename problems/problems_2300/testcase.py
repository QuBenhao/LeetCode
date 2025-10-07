from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 1, 3], [1, 2, 3, 4, 5], 7], Output=[4, 0, 3]))
		self.testcases.append(case(Input=[[3, 1, 2], [8, 5, 8], 16], Output=[2, 0, 2]))

	def get_testcases(self):
		return self.testcases
