from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 2], [3, 9, 4]], Output=[[1, 3, 2], [3, 4, 3], [4, 9, 4]]))
		self.testcases.append(case(Input=[[1, 3, 2], [2, 5, 3], [2, 8, 3]], Output=[[1, 3, 2], [3, 8, 3]]))
		self.testcases.append(case(Input=[[1, 2, 1], [5, 6, 1]], Output=[[1, 2, 1], [5, 6, 1]]))

	def get_testcases(self):
		return self.testcases
