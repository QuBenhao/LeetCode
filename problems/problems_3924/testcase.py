from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, [[0, 1, 5], [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]], 0, 3, 1], Output=4))
		self.testcases.append(case(Input=[6, [[0, 1, 3], [1, 2, 4], [3, 4, 5], [4, 5, 6]], 0, 4, 1], Output=-1))
		self.testcases.append(case(Input=[4, [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]], 0, 0, 0], Output=0))

	def get_testcases(self):
		return self.testcases
