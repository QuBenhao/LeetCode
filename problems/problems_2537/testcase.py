from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 1, 1, 1], 10], Output=1))
		self.testcases.append(case(Input=[[3, 1, 4, 3, 2, 2, 4], 2], Output=4))

	def get_testcases(self):
		return self.testcases
