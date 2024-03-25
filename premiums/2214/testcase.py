from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 7, 4, 3], 4], Output=13))
		self.testcases.append(case(Input=[[2, 5, 3, 4], 7], Output=10))
		self.testcases.append(case(Input=[[3, 3, 3], 0], Output=10))

	def get_testcases(self):
		return self.testcases
