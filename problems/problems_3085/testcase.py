from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabcaba', 0], Output=3))
		self.testcases.append(case(Input=['dabdcbdcdcd', 2], Output=2))
		self.testcases.append(case(Input=['aaabaaa', 2], Output=1))

	def get_testcases(self):
		return self.testcases
