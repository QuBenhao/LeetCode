from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9], Output=[1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]))
		self.testcases.append(case(Input=[5, 1, 7], Output=[1, None, 5, None, 7]))

	def get_testcases(self):
		return self.testcases
