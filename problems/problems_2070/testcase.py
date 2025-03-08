from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]], Output=[2, 4, 5, 5, 6, 6]))
		self.testcases.append(case(Input=[[[1, 2], [1, 2], [1, 3], [1, 4]], [1]], Output=[4]))
		self.testcases.append(case(Input=[[[10, 1000]], [5]], Output=[0]))

	def get_testcases(self):
		return self.testcases
