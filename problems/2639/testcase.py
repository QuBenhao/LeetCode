from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1], [22], [333]], Output=[3]))
		self.testcases.append(case(Input=[[-15, 1, 3], [15, 7, 12], [5, 6, -2]], Output=[3, 1, 2]))

	def get_testcases(self):
		return self.testcases
