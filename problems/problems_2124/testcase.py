from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaabbb", Output=True))
		self.testcases.append(case(Input="abab", Output=False))
		self.testcases.append(case(Input="bbb", Output=True))

	def get_testcases(self):
		return self.testcases
