from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, None, 4], Output=[4]))
		self.testcases.append(case(Input=[7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], Output=[6, 2]))
		self.testcases.append(case(Input=[11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22], Output=[77, 55, 33, 66, 44, 22]))

	def get_testcases(self):
		return self.testcases
