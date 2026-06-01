from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 8], [4, 1], [6], [3]], Output=9))
		self.testcases.append(case(Input=[[5], [3], [1], [10]], Output=14))

	def get_testcases(self):
		return self.testcases
