from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 7]], Output=[4]))
		self.testcases.append(case(Input=[[2, 5, 3], [7, 7, 4]], Output=[2, 2]))

	def get_testcases(self):
		return self.testcases
