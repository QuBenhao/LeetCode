from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3], Output="30"))
		self.testcases.append(case(Input=[2, 17], Output="98"))
		self.testcases.append(case(Input=[1, 10], Output=""))

	def get_testcases(self):
		return self.testcases
