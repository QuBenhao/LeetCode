from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 6, 7, 8], [1, 7, 2], [2, 9, 5]], Output=[5, 6, 8, 9]))
		self.testcases.append(case(Input=[[1, 1, 3, 3], [1, 3], [2, 2]], Output=[2]))
		self.testcases.append(case(Input=[[3,4],[4,3,1,2,2,3,2,4,1],[3,1,2,2,3,2,4,1,1]], Output=[1]))

	def get_testcases(self):
		return self.testcases
