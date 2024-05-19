from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6]], [[5, 3, 4], [5, 3, 6]]], Output=[0, 2]))
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], [[0, 1, 2]]], Output=[1]))
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], [[0, 0, 0]]], Output=[0]))

	def get_testcases(self):
		return self.testcases
