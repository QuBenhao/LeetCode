from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 2], 4], Output=5))
		self.testcases.append(case(Input=[[5, 5, 5, 5], 0], Output=10))
		self.testcases.append(case(Input=[[1, 2, 3], 0], Output=3))

	def get_testcases(self):
		return self.testcases
