from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]], Output=4))
		self.testcases.append(case(Input=[2, [[2, 1], [1, 8], [2, 6]]], Output=2))
		self.testcases.append(case(Input=[4, [[4, 3], [1, 4], [4, 6], [1, 7]]], Output=4))

	def get_testcases(self):
		return self.testcases
