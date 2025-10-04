from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]], Output=[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))
		self.testcases.append(case(Input=[[1]], Output=[[0, 0]]))

	def get_testcases(self):
		return self.testcases
