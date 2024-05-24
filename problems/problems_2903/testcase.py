from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 1, 4, 1], 2, 4], Output=[0, 3]))
		self.testcases.append(case(Input=[[2, 1], 0, 0], Output=[0, 0]))
		self.testcases.append(case(Input=[[1, 2, 3], 2, 4], Output=[-1, -1]))

	def get_testcases(self):
		return self.testcases
