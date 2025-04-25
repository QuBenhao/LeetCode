from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8], Output=[30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]))
		self.testcases.append(case(Input=[0, None, 1], Output=[1, None, 1]))
		self.testcases.append(case(Input=[1, 0, 2], Output=[3, 3, 2]))
		self.testcases.append(case(Input=[3, 2, 4, 1], Output=[7, 9, 4, 10]))

	def get_testcases(self):
		return self.testcases
