from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 1], 2], Output=[3, 4, 1, 2]))
		self.testcases.append(case(Input=[[], 1], Output=[1]))
		self.testcases.append(case(Input=[[1], 0], Output=[1, 0]))

	def get_testcases(self):
		return self.testcases
