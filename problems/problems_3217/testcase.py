from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], [1, 2, 3, 4, 5]], Output=[4, 5]))
		self.testcases.append(case(Input=[[1], [1, 2, 1, 2, 1, 2]], Output=[2, 2, 2]))
		self.testcases.append(case(Input=[[5], [1, 2, 3, 4]], Output=[1, 2, 3, 4]))

	def get_testcases(self):
		return self.testcases
