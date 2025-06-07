from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 7, 9, 8, 2], 2], Output=14))
		self.testcases.append(case(Input=[[12, 16, 19, 19, 8, 1, 19, 13, 9], 3], Output=36))

	def get_testcases(self):
		return self.testcases
