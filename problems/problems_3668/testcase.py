from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 1, 2, 5, 4], [1, 3, 4]], Output=[3, 1, 4]))
		self.testcases.append(case(Input=[[1, 4, 5, 3, 2], [2, 5]], Output=[5, 2]))

	def get_testcases(self):
		return self.testcases
