from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], Output=[20, 24]))
		self.testcases.append(case(Input=[[1, 2, 3], [1, 2, 3], [1, 2, 3]], Output=[1, 1]))

	def get_testcases(self):
		return self.testcases
