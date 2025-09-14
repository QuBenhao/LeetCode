from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 3, 2, 4], 5], Output=[False, False, True, True]))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 3], Output=[True, True, True, True, True]))

	def get_testcases(self):
		return self.testcases
