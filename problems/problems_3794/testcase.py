from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 2], Output="bacd"))
		self.testcases.append(case(Input=['xyz', 3], Output="zyx"))
		self.testcases.append(case(Input=['hey', 1], Output="hey"))

	def get_testcases(self):
		return self.testcases
