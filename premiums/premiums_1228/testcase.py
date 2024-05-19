from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 7, 11, 13], Output=9))
		self.testcases.append(case(Input=[15, 13, 12], Output=14))

	def get_testcases(self):
		return self.testcases
