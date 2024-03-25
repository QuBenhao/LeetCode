from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 5, 2, 3], 3], Output=[5, 2, 3]))
		self.testcases.append(case(Input=[[1, 4, 5, 2, 3], 4], Output=[4, 5, 2, 3]))
		self.testcases.append(case(Input=[[1, 4, 5, 2, 3], 1], Output=[5]))

	def get_testcases(self):
		return self.testcases
