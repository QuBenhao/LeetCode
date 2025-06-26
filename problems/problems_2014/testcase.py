from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['letsleetcode', 2], Output="let"))
		self.testcases.append(case(Input=['bb', 2], Output="b"))
		self.testcases.append(case(Input=['ab', 2], Output=""))

	def get_testcases(self):
		return self.testcases
