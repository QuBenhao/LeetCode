from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 2], [1, 2]], Output=[2, 1]))
		self.testcases.append(case(Input=[[4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]], Output=[3, 4]))
		self.testcases.append(case(Input=[[3, 4, 2, 3], [1, 5]], Output=[0, 0]))

	def get_testcases(self):
		return self.testcases
