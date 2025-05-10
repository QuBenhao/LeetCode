from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [4, -8, -6, 3, 7, -2, 5], 2], Output=27))
		self.testcases.append(case(Input=[[[0, 1], [1, 2], [2, 3], [3, 4]], [-1, 3, -2, 4, -5], 2], Output=9))
		self.testcases.append(case(Input=[[[0, 1], [0, 2]], [0, -1, -2], 3], Output=3))

	def get_testcases(self):
		return self.testcases
