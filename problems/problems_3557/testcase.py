from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abcdeafdef", Output=2))
		self.testcases.append(case(Input="bcdaaaab", Output=1))

	def get_testcases(self):
		return self.testcases
