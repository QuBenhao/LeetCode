from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[2, 8], [6, 3], [8, 6]], 5, 4], Output=9))
		self.testcases.append(case(Input=[[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4], Output=14))
		self.testcases.append(case(Input=[[[0, 3], [6, 4], [8, 5]], 3, 2], Output=0))

	def get_testcases(self):
		return self.testcases
