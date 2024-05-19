from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]], Output=[1, 0, 0, 0, 0, 1, 2]))
		self.testcases.append(case(Input=[9, [[0, 1], [1, 2], [0, 2], [2, 6], [6, 7], [6, 8], [0, 3], [3, 4], [3, 5]]], Output=[0, 0, 0, 1, 2, 2, 1, 2, 2]))

	def get_testcases(self):
		return self.testcases
