from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 2], 2], Output=6))
		self.testcases.append(case(Input=[[5, 1, 1, 1], 0], Output=8))

	def get_testcases(self):
		return self.testcases
