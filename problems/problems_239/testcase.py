from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, -1, -3, 5, 3, 6, 7], 3], Output=[3, 3, 5, 5, 6, 7]))
		self.testcases.append(case(Input=[[1], 1], Output=[1]))
		self.testcases.append(case(Input=[[1,-1],1], Output=[1,-1]))

	def get_testcases(self):
		return self.testcases
