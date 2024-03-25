from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 1], [2, 2], [3, 3], [5, 5]], [4, 4], [0, 0]], Output=3))
		self.testcases.append(case(Input=[[[1, 1], [2, 2], [3, 3]], [1000, 1000], [0, 0]], Output=3))

	def get_testcases(self):
		return self.testcases
