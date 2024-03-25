from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 2, 4], Output=[4, 2, 1, 0]))
		self.testcases.append(case(Input=[10, 20, 50, 10], Output=[50, 20, 10, 10]))

	def get_testcases(self):
		return self.testcases
