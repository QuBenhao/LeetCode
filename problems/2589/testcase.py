from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 1], [4, 5, 1], [1, 5, 2]], Output=2))
		self.testcases.append(case(Input=[[1, 3, 2], [2, 5, 3], [5, 6, 2]], Output=4))

	def get_testcases(self):
		return self.testcases
