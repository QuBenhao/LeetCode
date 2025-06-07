from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3], [-1, 0]], Output=8))
		self.testcases.append(case(Input=[[1, 5, 2], [-1, 0, 0]], Output=15))
		self.testcases.append(case(Input=[[34, 1, 2], [-1, 0, 1]], Output=42))
		self.testcases.append(case(Input=[[3, 22, 5], [-1, 0, 1]], Output=18))

	def get_testcases(self):
		return self.testcases
