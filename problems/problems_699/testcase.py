from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [2, 3], [6, 1]], Output=[2, 5, 5]))
		self.testcases.append(case(Input=[[100, 100], [200, 100]], Output=[100, 100]))

	def get_testcases(self):
		return self.testcases
