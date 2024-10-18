from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[7, 2, 4, 3], [5, 6, 4]], Output=[7, 8, 0, 7]))
		self.testcases.append(case(Input=[[2, 4, 3], [5, 6, 4]], Output=[8, 0, 7]))
		self.testcases.append(case(Input=[[0], [0]], Output=[0]))

	def get_testcases(self):
		return self.testcases
