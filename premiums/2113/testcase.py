from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 2], [[0, 2], [2, 0], [3, 2], [5, 0]]], Output=[2, 2, -1, 0]))
		self.testcases.append(case(Input=[[2], [[0, 0], [1, 0], [2, 0], [3, 0]]], Output=[2, -1, 2, -1]))

	def get_testcases(self):
		return self.testcases
