from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[2, 4], [0, 2], [0, 4]]], Output=[3, 2, 1]))
		self.testcases.append(case(Input=[4, [[0, 3], [0, 2]]], Output=[1, 1]))

	def get_testcases(self):
		return self.testcases
