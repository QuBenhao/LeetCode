from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 4], [0, 2, 2]], Output=[1, 2, 2]))
		self.testcases.append(case(Input=[[4, 4, 2, 1], [5, 3, 1, 0]], Output=[4, 2, 1, 1]))
		self.testcases.append(case(Input=[[2, 2], [0, 0]], Output=[2, 2]))

	def get_testcases(self):
		return self.testcases
