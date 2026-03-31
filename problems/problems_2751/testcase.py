from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 4, 3, 2, 1], [2, 17, 9, 15, 10], 'RRRRR'], Output=[2, 17, 9, 15, 10]))
		self.testcases.append(case(Input=[[3, 5, 2, 6], [10, 10, 15, 12], 'RLRL'], Output=[14]))
		self.testcases.append(case(Input=[[1, 2, 5, 6], [10, 10, 11, 11], 'RLRL'], Output=[]))

	def get_testcases(self):
		return self.testcases
