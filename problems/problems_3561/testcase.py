from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abc", Output="c"))
		self.testcases.append(case(Input="adcb", Output=""))
		self.testcases.append(case(Input="zadb", Output="db"))

	def get_testcases(self):
		return self.testcases
