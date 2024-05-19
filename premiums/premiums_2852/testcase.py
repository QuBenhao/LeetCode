from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-1, 1, -1], [5, -1, 4], [-1, 3, -1]], Output=39))
		self.testcases.append(case(Input=[[-1, 3, 4], [-1, -1, -1], [3, -1, -1]], Output=13))
		self.testcases.append(case(Input=[[1]], Output=0))

	def get_testcases(self):
		return self.testcases
