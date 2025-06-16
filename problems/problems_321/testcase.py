from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5], Output=[9, 8, 6, 5, 3]))
		self.testcases.append(case(Input=[[6, 7], [6, 0, 4], 5], Output=[6, 7, 6, 0, 4]))
		self.testcases.append(case(Input=[[3, 9], [8, 9], 3], Output=[9, 8, 9]))
		self.testcases.append(case(Input=[[8,9],[3,9],3], Output=[9,8,9]))
		self.testcases.append(case(Input=[[6,7,5],[4,8,1],3], Output=[8,7,5]))

	def get_testcases(self):
		return self.testcases
