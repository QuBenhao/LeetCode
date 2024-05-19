from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 10, 5], [3, 0, 5, 3], 5], Output=[5, 10]))
		self.testcases.append(case(Input=[[1], [0], 1], Output=[1]))

	def get_testcases(self):
		return self.testcases
