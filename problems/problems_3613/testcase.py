from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 1, 4], [1, 2, 3], [1, 3, 2], [3, 4, 6]], 2], Output=4))
		self.testcases.append(case(Input=[4, [[0, 1, 5], [1, 2, 5], [2, 3, 5]], 1], Output=5))

	def get_testcases(self):
		return self.testcases
