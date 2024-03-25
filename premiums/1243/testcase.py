from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, 2, 3, 4], Output=[6, 3, 3, 4]))
		self.testcases.append(case(Input=[1, 6, 3, 4, 3, 5], Output=[1, 4, 4, 4, 4, 5]))

	def get_testcases(self):
		return self.testcases
