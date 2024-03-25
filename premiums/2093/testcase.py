from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]], 1], Output=9))
		self.testcases.append(case(Input=[4, [[1, 3, 17], [1, 2, 7], [3, 2, 5], [0, 1, 6], [3, 0, 20]], 20], Output=8))
		self.testcases.append(case(Input=[4, [[0, 1, 3], [2, 3, 2]], 0], Output=-1))

	def get_testcases(self):
		return self.testcases
