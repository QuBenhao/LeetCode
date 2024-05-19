from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], [2, 8, 3, 6, 2, 5]], Output=24))
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], [4, 6, 1]], Output=0))

	def get_testcases(self):
		return self.testcases
