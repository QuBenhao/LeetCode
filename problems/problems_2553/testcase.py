from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[13, 25, 83, 77], Output=[1, 3, 2, 5, 8, 3, 7, 7]))
		self.testcases.append(case(Input=[7, 1, 3, 9], Output=[7, 1, 3, 9]))

	def get_testcases(self):
		return self.testcases
