from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 4, 5], [1, 2, 6], [7, 4, 6]], Output=4))
		self.testcases.append(case(Input=[[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]], Output=2))
		self.testcases.append(case(Input=[[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]], Output=3))

	def get_testcases(self):
		return self.testcases
