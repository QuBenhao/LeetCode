from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 2, 4], [2, 3, 1, 2, 3]], Output=[0, 3]))
		self.testcases.append(case(Input=[[1, 2, 4, 3, 2, 5], [1, 4, 2, 3, 5, 1]], Output=[1, 4]))

	def get_testcases(self):
		return self.testcases
