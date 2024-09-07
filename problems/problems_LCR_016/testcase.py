from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abcabcbb", Output=3))
		self.testcases.append(case(Input="bbbbb", Output=1))
		self.testcases.append(case(Input="pwwkew", Output=3))

	def get_testcases(self):
		return self.testcases
