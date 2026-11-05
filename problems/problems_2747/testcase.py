from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]], Output=[1, 2]))
		self.testcases.append(case(Input=[3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]], Output=[0, 1]))

	def get_testcases(self):
		return self.testcases
