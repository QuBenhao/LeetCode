from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 5, 1, 3], 3.714286, 2], Output=[4, 3]))
		self.testcases.append(case(Input=[[1], 0.0, 1], Output=[1]))

	def get_testcases(self):
		return self.testcases
