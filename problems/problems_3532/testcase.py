from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [1, 3], 1, [[0, 0], [0, 1]]], Output=[True, False]))
		self.testcases.append(case(Input=[4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]], Output=[False, False, True, True]))

	def get_testcases(self):
		return self.testcases
