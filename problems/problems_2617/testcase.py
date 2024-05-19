from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]], Output=4))
		self.testcases.append(case(Input=[[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]], Output=3))
		self.testcases.append(case(Input=[[2, 1, 0], [1, 0, 0]], Output=-1))
		self.testcases.append(case(Input=[[0]], Output=1))

	def get_testcases(self):
		return self.testcases
