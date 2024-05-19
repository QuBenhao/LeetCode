from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', [1, 2, 1]], Output=[1, 2, 0]))
		self.testcases.append(case(Input=['abc', [4, 1]], Output=[3, 0]))

	def get_testcases(self):
		return self.testcases
