from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 7, 1, 3, 6, 9], Output=[4, 7, 2, 9, 6, 3, 1]))
		self.testcases.append(case(Input=[2, 1, 3], Output=[2, 3, 1]))
		self.testcases.append(case(Input=[], Output=[]))

	def get_testcases(self):
		return self.testcases
