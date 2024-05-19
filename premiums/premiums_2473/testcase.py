from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]], [56, 42, 102, 301], 2], Output=[54, 42, 48, 51]))
		self.testcases.append(case(Input=[3, [[1, 2, 5], [2, 3, 1], [3, 1, 2]], [2, 3, 1], 3], Output=[2, 3, 1]))

	def get_testcases(self):
		return self.testcases
