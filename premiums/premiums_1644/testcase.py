from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], Output=3))
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], Output=5))
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 10], Output=None))

	def get_testcases(self):
		return self.testcases
