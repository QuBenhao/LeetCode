from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4], 1], Output=8))
		self.testcases.append(case(Input=[[3, 5, 7], 2], Output=14))
		self.testcases.append(case(Input=[[5, 5, 5], 1], Output=15))
		self.testcases.append(case(Input=[[6,12,6,12,6,12,18,12], 3], Output=84))

	def get_testcases(self):
		return self.testcases
