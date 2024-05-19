from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4], Output=11))
		self.testcases.append(case(Input=[[1, 2, 4, 1], 3, 3], Output=4))

	def get_testcases(self):
		return self.testcases
