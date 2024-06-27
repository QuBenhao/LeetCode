from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="cbabc", Output="baabc"))
		self.testcases.append(case(Input="aa", Output="az"))
		self.testcases.append(case(Input="acbbc", Output="abaab"))
		self.testcases.append(case(Input="leetcode", Output="kddsbncd"))

	def get_testcases(self):
		return self.testcases
