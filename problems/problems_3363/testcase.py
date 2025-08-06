from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]], Output=100))
		self.testcases.append(case(Input=[[1, 1], [1, 1]], Output=4))

	def get_testcases(self):
		return self.testcases
