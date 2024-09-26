from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabaaaacaabc', 2], Output=8))
		self.testcases.append(case(Input=['a', 1], Output=-1))

	def get_testcases(self):
		return self.testcases
