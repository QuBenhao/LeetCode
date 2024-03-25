from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 7], 80], Output=2.0))
		self.testcases.append(case(Input=[[2, 4, 6], 50], Output=3.5))
		self.testcases.append(case(Input=[[3, 3, 3, 3], 40], Output=3.0))

	def get_testcases(self):
		return self.testcases
