from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1, 0, 3], Output=[[1, 2, 3, 4], [13, 14, 15, 8], [9, 10, 11, 12], [5, 6, 7, 16]]))
		self.testcases.append(case(Input=[[[3, 4, 2, 3], [2, 3, 4, 2]], 0, 2, 2], Output=[[3, 4, 4, 2], [2, 3, 2, 3]]))

	def get_testcases(self):
		return self.testcases
