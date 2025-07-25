from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 4, 3], Output=[1, 2, 3, 4]))
		self.testcases.append(case(Input=[[1, 1, 2, 3, 4, 5], 4, -1], Output=[1, 1, 2, 3]))

	def get_testcases(self):
		return self.testcases
