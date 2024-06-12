from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[3, 2], [5, 1], [10, 1]], 2], Output=17))
		self.testcases.append(case(Input=[[[3, 1], [3, 1], [2, 2], [5, 3]], 3], Output=19))
		self.testcases.append(case(Input=[[[1, 1], [2, 1], [3, 1]], 3], Output=7))

	def get_testcases(self):
		return self.testcases
