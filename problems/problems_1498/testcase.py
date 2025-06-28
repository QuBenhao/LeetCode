from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 6, 7], 9], Output=4))
		self.testcases.append(case(Input=[[3, 3, 6, 8], 10], Output=6))
		self.testcases.append(case(Input=[[2, 3, 3, 4, 6, 7], 12], Output=61))

	def get_testcases(self):
		return self.testcases
