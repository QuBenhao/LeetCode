from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]]], Output=1))
		self.testcases.append(case(Input=[[[1, 1], [1, 3], [1, 5]], [[5, 5], [5, 7], [5, 9]]], Output=4))
		self.testcases.append(case(Input=[[[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]]], Output=1))
		self.testcases.append(case(Input=[[[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]]], Output=0))

	def get_testcases(self):
		return self.testcases
