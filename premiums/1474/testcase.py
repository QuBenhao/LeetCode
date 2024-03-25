from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2, 3], Output=[1, 2, 6, 7, 11, 12]))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1, 3], Output=[1, 5, 9]))

	def get_testcases(self):
		return self.testcases
