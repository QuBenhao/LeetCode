from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 7, 1, 4], 3], Output=[12, 10, 16, 13]))
		self.testcases.append(case(Input=[[1, 2, 3, 4], 0], Output=[0, 0, 0, 0]))
		self.testcases.append(case(Input=[[2, 4, 9, 3], -2], Output=[12, 5, 6, 13]))

	def get_testcases(self):
		return self.testcases
