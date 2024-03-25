from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 3, 4, 1], [5, 3, 3, 4, 1]], Output=3))
		self.testcases.append(case(Input=[[1, 2, 2, 3, 4], [3, 4, 1, 2]], Output=3))
		self.testcases.append(case(Input=[[1, 2, 3], [1, 2, 3, 4]], Output=1))

	def get_testcases(self):
		return self.testcases
