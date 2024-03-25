from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7], Output=[7, 2, None, 5, 4, 3, 6, None, None, None, 1, None, None, 0, 8]))
		self.testcases.append(case(Input=[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0], Output=[0, 1, None, 3, 8, 5, None, None, None, 6, 2, None, None, 7, 4]))

	def get_testcases(self):
		return self.testcases
