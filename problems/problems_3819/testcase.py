from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, -2, 3, -4], 3], Output=[3, -2, 1, -4]))
		self.testcases.append(case(Input=[[-3, -2, 7], 1], Output=[-3, -2, 7]))
		self.testcases.append(case(Input=[[5, 4, -9, 6], 2], Output=[6, 5, -9, 4]))

	def get_testcases(self):
		return self.testcases
