from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 0], [2, 1]], [[1, 2], [3, 3]]], Output=6))
		self.testcases.append(case(Input=[[[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]], Output=4))
		self.testcases.append(case(Input=[[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]], [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]], Output=4995))

	def get_testcases(self):
		return self.testcases
