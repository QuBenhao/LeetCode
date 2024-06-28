from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="51230100", Output="512301"))
		self.testcases.append(case(Input="123", Output="123"))

	def get_testcases(self):
		return self.testcases
