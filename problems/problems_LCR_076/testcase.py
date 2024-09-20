from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 1, 5, 6, 4], 2], Output=5))
		self.testcases.append(case(Input=[[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], Output=4))

	def get_testcases(self):
		return self.testcases
