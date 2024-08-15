from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 3, 3, 2], [0, 3, 3, 2]], Output=12))
		self.testcases.append(case(Input=[[2, 3, 5, 7, 7, 7, 5], [0, 7, 5]], Output=17))
		self.testcases.append(case(Input=[[1, 2, 3, 4], [2]], Output=-1))

	def get_testcases(self):
		return self.testcases
