from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6], Output=2))
		self.testcases.append(case(Input=[7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3], Output=3))

	def get_testcases(self):
		return self.testcases
