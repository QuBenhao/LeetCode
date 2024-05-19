from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 12, -5, -6, 50, 3], 4], Output=12.75))
		self.testcases.append(case(Input=[[5], 1], Output=5.0))

	def get_testcases(self):
		return self.testcases
