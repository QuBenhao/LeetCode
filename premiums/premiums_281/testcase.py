from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [3, 4, 5, 6]], Output=[1, 3, 2, 4, 5, 6]))
		self.testcases.append(case(Input=[[1], []], Output=[1]))
		self.testcases.append(case(Input=[[], [1]], Output=[1]))

	def get_testcases(self):
		return self.testcases
