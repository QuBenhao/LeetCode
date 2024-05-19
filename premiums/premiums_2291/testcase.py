from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 4, 6, 2, 3], [8, 5, 4, 3, 5], 10], Output=6))
		self.testcases.append(case(Input=[[2, 2, 5], [3, 4, 10], 6], Output=5))
		self.testcases.append(case(Input=[[3, 3, 12], [0, 3, 15], 10], Output=0))

	def get_testcases(self):
		return self.testcases
