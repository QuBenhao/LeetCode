from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], 0, [2, 3]], Output=4))
		self.testcases.append(case(Input=[5, [[0, 1, 2], [0, 2, 4], [1, 3, 1], [2, 3, 3], [3, 4, 2]], 1, [0, 4]], Output=3))
		self.testcases.append(case(Input=[4, [[0, 1, 1], [1, 2, 3], [2, 3, 2]], 3, [0, 1]], Output=-1))

	def get_testcases(self):
		return self.testcases
