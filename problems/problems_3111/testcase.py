from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], 1], Output=2))
		self.testcases.append(case(Input=[[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], 2], Output=3))
		self.testcases.append(case(Input=[[[2, 3], [1, 2]], 0], Output=2))

	def get_testcases(self):
		return self.testcases
