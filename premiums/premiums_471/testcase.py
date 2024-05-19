from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaa", Output="aaa"))
		self.testcases.append(case(Input="5[a]", Output="5[a]"))
		self.testcases.append(case(Input="10[a]", Output="10[a]"))

	def get_testcases(self):
		return self.testcases
