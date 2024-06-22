from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcz', 26], Output="abda"))
		self.testcases.append(case(Input=['dc', 4], Output=""))

	def get_testcases(self):
		return self.testcases
