from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1], Output=[0, 1, 2, 3, 5]))
		self.testcases.append(case(Input=[4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3], Output=[0, 1, 3]))
		self.testcases.append(case(Input=[5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1], Output=[0, 1, 2, 3, 4]))

	def get_testcases(self):
		return self.testcases
