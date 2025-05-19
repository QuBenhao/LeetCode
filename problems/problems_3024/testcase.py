from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 3, 3], Output="equilateral"))
		self.testcases.append(case(Input=[3, 4, 5], Output="scalene"))
		self.testcases.append(case(Input=[8,4,2], Output="none"))
		self.testcases.append(case(Input=[5,3,8], Output="none"))

	def get_testcases(self):
		return self.testcases
