from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 7, 9, 10], 1], Output=5))
		self.testcases.append(case(Input=[[4, 7, 9, 10], 3], Output=8))
		self.testcases.append(case(Input=[[1, 2, 4], 3], Output=6))

	def get_testcases(self):
		return self.testcases
