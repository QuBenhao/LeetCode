from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 8, 5, 3], [1, 5, 2, 7], 8], Output=8))
		self.testcases.append(case(Input=[[3, 5, 7, 4], [2, 4, 3, 6], 7], Output=6))
		self.testcases.append(case(Input=[[2, 2, 2], [3, 5, 4], 5], Output=9))

	def get_testcases(self):
		return self.testcases
