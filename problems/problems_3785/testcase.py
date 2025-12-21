from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], [3, 2, 1]], Output=1))
		self.testcases.append(case(Input=[[4, 6, 6, 5], [4, 6, 5, 5]], Output=2))
		self.testcases.append(case(Input=[[7, 7], [8, 7]], Output=-1))
		self.testcases.append(case(Input=[[1, 2], [2, 1]], Output=0))

	def get_testcases(self):
		return self.testcases
