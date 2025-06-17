from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 4, 8, 7, 9, 3, 5, 1], 2], Output=[[1, 1, 3], [3, 4, 5], [7, 8, 9]]))
		self.testcases.append(case(Input=[[2, 4, 2, 2, 5, 2], 2], Output=[]))
		self.testcases.append(case(Input=[[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14], Output=[[2, 2, 12], [4, 8, 5], [5, 9, 7], [7, 8, 5], [5, 9, 10], [11, 12, 2]]))

	def get_testcases(self):
		return self.testcases
