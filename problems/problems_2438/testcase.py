from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[15, [[0, 1], [2, 2], [0, 3]]], Output=[2, 4, 64]))
		self.testcases.append(case(Input=[2, [[0, 0]]], Output=[2]))

	def get_testcases(self):
		return self.testcases
