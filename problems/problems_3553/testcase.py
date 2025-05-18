from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1, 2], [1, 2, 3], [1, 3, 5], [1, 4, 4], [2, 5, 6]], [[2, 3, 4], [0, 2, 5]]], Output=[12, 11]))
		self.testcases.append(case(Input=[[[1, 0, 8], [0, 2, 7]], [[0, 1, 2]]], Output=[15]))

	def get_testcases(self):
		return self.testcases
