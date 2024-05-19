from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4], [4, 7], [5, 8]], Output=[3, 3, 1]))
		self.testcases.append(case(Input=[[1, 4], [5, 8], [4, 7]], Output=[3, 3, 1]))
		self.testcases.append(case(Input=[[1, 5], [2, 4]], Output=[4, 0]))

	def get_testcases(self):
		return self.testcases
