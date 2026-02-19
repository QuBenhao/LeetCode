from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="11011000", Output="11100100"))
		self.testcases.append(case(Input="10", Output="10"))

	def get_testcases(self):
		return self.testcases
