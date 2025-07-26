from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 6, 3, 1, 5], 1, 2], Output=[4, 1, 1, 2, None, None, 6, 3, 1, 5]))
		self.testcases.append(case(Input=[[4, 2, None, 3, 1], 1, 3], Output=[4, 2, None, 1, 1, 3, None, None, 1]))

	def get_testcases(self):
		return self.testcases
