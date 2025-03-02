from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 2], Output=1))
		self.testcases.append(case(Input=['aabbc', 3], Output=0))
		self.testcases.append(case(Input=['leetcode', 8], Output=0))

	def get_testcases(self):
		return self.testcases
