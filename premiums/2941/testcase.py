from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 4, 4, 4, 2], 2], Output=48))
		self.testcases.append(case(Input=[[7, 3, 9, 4], 1], Output=81))

	def get_testcases(self):
		return self.testcases
