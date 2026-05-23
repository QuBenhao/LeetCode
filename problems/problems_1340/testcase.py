from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2], Output=4))
		self.testcases.append(case(Input=[[3, 3, 3, 3, 3], 3], Output=1))
		self.testcases.append(case(Input=[[7, 6, 5, 4, 3, 2, 1], 1], Output=7))

	def get_testcases(self):
		return self.testcases
