from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 20, 16, 12, 8], [14, 18, 10]], Output=-2))
		self.testcases.append(case(Input=[[3, 5, 5, 3], [7, 7]], Output=2))

	def get_testcases(self):
		return self.testcases
