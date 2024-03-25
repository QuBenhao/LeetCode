from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 1, 3, 3], Output=0))
		self.testcases.append(case(Input=[[3, 2], 2, 0, 1], Output=1))
		self.testcases.append(case(Input=[[6, 5, 0, 0], 2, 1, 5], Output=0))

	def get_testcases(self):
		return self.testcases
