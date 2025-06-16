from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1432219', 3], Output="1219"))
		self.testcases.append(case(Input=['10200', 1], Output="200"))
		self.testcases.append(case(Input=['10', 2], Output="0"))

	def get_testcases(self):
		return self.testcases
