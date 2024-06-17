from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2.0, 10], Output=1024.0))
		self.testcases.append(case(Input=[2.1, 3], Output=9.261))
		self.testcases.append(case(Input=[2.0, -2], Output=0.25))
		self.testcases.append(case(Input=[1.00000,-2147483648], Output=1.00000))

	def get_testcases(self):
		return self.testcases
