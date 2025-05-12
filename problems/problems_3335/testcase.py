from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcyy', 2], Output=7))
		self.testcases.append(case(Input=['azbk', 1], Output=5))

	def get_testcases(self):
		return self.testcases
