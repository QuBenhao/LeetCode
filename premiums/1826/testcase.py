from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 4, 5], [2, 1, 3, 4]], Output=1))
		self.testcases.append(case(Input=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 5]], Output=-1))
		self.testcases.append(case(Input=[[2, 3, 2, 2, 3, 2], [2, 3, 2, 3, 2, 7]], Output=2))

	def get_testcases(self):
		return self.testcases
