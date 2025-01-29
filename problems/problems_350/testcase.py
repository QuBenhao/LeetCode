from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 2, 1], [2, 2]], Output=[2, 2]))
		self.testcases.append(case(Input=[[4, 9, 5], [9, 4, 9, 8, 4]], Output=[4, 9]))

	def get_testcases(self):
		return self.testcases
