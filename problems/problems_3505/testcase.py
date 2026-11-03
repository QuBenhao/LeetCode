from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2], Output=8))
		self.testcases.append(case(Input=[[9, -2, -2, -2, 1, 5], 2, 2], Output=3))

	def get_testcases(self):
		return self.testcases
