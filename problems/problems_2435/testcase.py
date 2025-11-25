from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3], Output=2))
		self.testcases.append(case(Input=[[[0, 0]], 5], Output=1))
		self.testcases.append(case(Input=[[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1], Output=10))

	def get_testcases(self):
		return self.testcases
