from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 2], [1, 1, 5, 2, 3], [2, 3, 4, 5, 6]], Output=[5, 16, 10]))
		self.testcases.append(case(Input=[[5], [2, 3, 1, 2], [10, 6, 5, 2]], Output=[23]))
		self.testcases.append(case(Input=[[4, 4], [5, 7, 8], [1, 1, 1]], Output=[0, 0]))

	def get_testcases(self):
		return self.testcases
