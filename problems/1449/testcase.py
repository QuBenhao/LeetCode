from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 3, 2, 5, 6, 7, 2, 5, 5], 9], Output="7772"))
		self.testcases.append(case(Input=[[7, 6, 5, 5, 5, 6, 8, 7, 8], 12], Output="85"))
		self.testcases.append(case(Input=[[2, 4, 6, 2, 4, 6, 4, 4, 4], 5], Output="0"))

	def get_testcases(self):
		return self.testcases
