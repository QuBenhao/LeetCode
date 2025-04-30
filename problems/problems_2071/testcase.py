from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 1], [0, 3, 3], 1, 1], Output=3))
		self.testcases.append(case(Input=[[5, 4], [0, 0, 0], 1, 5], Output=1))
		self.testcases.append(case(Input=[[10, 15, 30], [0, 10, 10, 10, 10], 3, 10], Output=2))

	def get_testcases(self):
		return self.testcases
