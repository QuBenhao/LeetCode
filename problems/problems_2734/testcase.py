from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="cbabc", Output=None))
		self.testcases.append(case(Input="aa", Output=None))
		self.testcases.append(case(Input="acbbc", Output=None))
		self.testcases.append(case(Input="leetcode", Output=None))

	def get_testcases(self):
		return self.testcases
