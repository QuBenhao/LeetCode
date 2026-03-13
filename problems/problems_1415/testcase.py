from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3], Output="c"))
		self.testcases.append(case(Input=[1, 4], Output=""))
		self.testcases.append(case(Input=[3, 9], Output="cab"))

	def get_testcases(self):
		return self.testcases
