from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="ABC", Output=10))
		self.testcases.append(case(Input="ABA", Output=8))
		self.testcases.append(case(Input="LEETCODE", Output=92))

	def get_testcases(self):
		return self.testcases
