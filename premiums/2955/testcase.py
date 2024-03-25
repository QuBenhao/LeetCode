from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcaab', [[0, 0], [1, 4], [2, 5], [0, 5]]], Output=[1, 5, 5, 10]))
		self.testcases.append(case(Input=['abcd', [[0, 3]]], Output=[4]))

	def get_testcases(self):
		return self.testcases
