from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 9, 1, 3, 9, 5], 9, 1], Output=[1, 2, 3, 4, 5, 6]))
		self.testcases.append(case(Input=[[2, 2, 2, 2, 2], 2, 2], Output=[0, 1, 2, 3, 4]))
		self.testcases.append(case(Input=[[2,1,1,1,2],2,1], Output=[0,1,3,4]))

	def get_testcases(self):
		return self.testcases
