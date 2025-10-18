from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['5525', 9, 2], Output="2050"))
		self.testcases.append(case(Input=['74', 5, 1], Output="24"))
		self.testcases.append(case(Input=['0011', 4, 2], Output="0011"))

	def get_testcases(self):
		return self.testcases
