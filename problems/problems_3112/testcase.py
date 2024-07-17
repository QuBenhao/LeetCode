from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 1, 5]], Output=[0, -1, 4]))
		self.testcases.append(case(Input=[3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 3, 5]], Output=[0, 2, 3]))
		self.testcases.append(case(Input=[2, [[0, 1, 1]], [1, 1]], Output=[0, -1]))

	def get_testcases(self):
		return self.testcases
