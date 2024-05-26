from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 4, 3], 4, 2], Output=[6, 6]))
		self.testcases.append(case(Input=[[1, 5, 6], 3, 4], Output=[2, 3, 2, 2]))
		self.testcases.append(case(Input=[[1, 2, 3, 4], 6, 4], Output=[]))
		self.testcases.append(case(Input=[[6,3,4,3,5,3], 1, 6], Output=[]))

	def get_testcases(self):
		return self.testcases
