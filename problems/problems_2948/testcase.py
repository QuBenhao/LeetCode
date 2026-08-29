from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 5, 3, 9, 8], 2], Output=[1, 3, 5, 8, 9]))
		self.testcases.append(case(Input=[[1, 7, 6, 18, 2, 1], 3], Output=[1, 6, 7, 18, 1, 2]))
		self.testcases.append(case(Input=[[1, 7, 28, 19, 10], 3], Output=[1, 7, 28, 19, 10]))

	def get_testcases(self):
		return self.testcases
