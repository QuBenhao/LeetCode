from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 1, 4, None, 2], 1], Output=1))
		self.testcases.append(case(Input=[[5, 3, 6, 2, 4, None, None, 1], 3], Output=3))

	def get_testcases(self):
		return self.testcases
