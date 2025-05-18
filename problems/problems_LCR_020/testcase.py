from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abc", Output=3))
		self.testcases.append(case(Input="aaa", Output=6))

	def get_testcases(self):
		return self.testcases
