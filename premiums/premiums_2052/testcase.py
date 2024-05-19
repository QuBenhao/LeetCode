from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['i love leetcode', 12], Output=36))
		self.testcases.append(case(Input=['apples and bananas taste great', 7], Output=21))
		self.testcases.append(case(Input=['a', 5], Output=0))

	def get_testcases(self):
		return self.testcases
