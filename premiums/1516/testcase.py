from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, None, 2, 3, None, 4, 5, None, 6, None, 7, 8], 4, 1], Output=[1, None, 2, 3, 4, None, 5, None, 6, None, 7, 8]))
		self.testcases.append(case(Input=[[1, None, 2, 3, None, 4, 5, None, 6, None, 7, 8], 7, 4], Output=[1, None, 2, 3, None, 4, 5, None, 6, None, 7, 8]))
		self.testcases.append(case(Input=[[1, None, 2, 3, None, 4, 5, None, 6, None, 7, 8], 3, 8], Output=[1, None, 2, None, 4, 5, None, 7, 8, None, None, None, 3, None, 6]))

	def get_testcases(self):
		return self.testcases
