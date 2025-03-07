from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 1, 1], 7, 6, 12, 1], Output=14))
		self.testcases.append(case(Input=[[2, 4, 5, 3], 10, 5, 2, 6], Output=30))

	def get_testcases(self):
		return self.testcases
