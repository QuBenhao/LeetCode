from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abac', 'cab'], Output="cabac"))
		self.testcases.append(case(Input=['aaaaaaaa', 'aaaaaaaa'], Output="aaaaaaaa"))

	def get_testcases(self):
		return self.testcases
