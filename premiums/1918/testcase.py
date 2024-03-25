from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 3], 4], Output=3))
		self.testcases.append(case(Input=[[3, 3, 5, 5], 7], Output=10))

	def get_testcases(self):
		return self.testcases
