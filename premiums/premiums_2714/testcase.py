from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[0, 1, 4], [0, 2, 2], [2, 3, 6]], 1, 3, 2], Output=2))
		self.testcases.append(case(Input=[7, [[3, 1, 9], [3, 2, 4], [4, 0, 9], [0, 5, 6], [3, 6, 2], [6, 0, 4], [1, 2, 4]], 4, 1, 2], Output=6))
		self.testcases.append(case(Input=[5, [[0, 4, 2], [0, 1, 3], [0, 2, 1], [2, 1, 4], [1, 3, 4], [3, 4, 7]], 2, 3, 1], Output=3))

	def get_testcases(self):
		return self.testcases
