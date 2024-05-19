from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 9, 22, 10, 19], [[18, 4], [5, 2]]], Output=[34, -21]))
		self.testcases.append(case(Input=[[1, 5, 4, 3, 7, 11, 9], [[5, 4], [5, 7], [7, 3], [4, 5]]], Output=[4, 16, 7, 1]))
		self.testcases.append(case(Input=[[5, 6, 7], [[10, 1], [5, 3], [3, 3]]], Output=[5, 12, 0]))

	def get_testcases(self):
		return self.testcases
