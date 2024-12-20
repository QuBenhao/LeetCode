from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2], Output=[[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]))
		self.testcases.append(case(Input=[[[3, 4], [5, 6]], 0], Output=[[5, 6], [3, 4]]))

	def get_testcases(self):
		return self.testcases
