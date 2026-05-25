from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaAbcBC", Output=3))
		self.testcases.append(case(Input="abc", Output=0))
		self.testcases.append(case(Input="abBCab", Output=1))

	def get_testcases(self):
		return self.testcases
