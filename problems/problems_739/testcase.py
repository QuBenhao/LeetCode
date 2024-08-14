from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[73, 74, 75, 71, 69, 72, 76, 73], Output=[1, 1, 4, 2, 1, 1, 0, 0]))
		self.testcases.append(case(Input=[30, 40, 50, 60], Output=[1, 1, 1, 0]))
		self.testcases.append(case(Input=[30, 60, 90], Output=[1, 1, 0]))

	def get_testcases(self):
		return self.testcases
