from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[40, 10, 20, 30], Output=[4, 1, 2, 3]))
		self.testcases.append(case(Input=[100, 100, 100], Output=[1, 1, 1]))
		self.testcases.append(case(Input=[37, 12, 28, 9, 100, 56, 80, 5, 12], Output=[5, 3, 4, 2, 8, 6, 7, 1, 3]))

	def get_testcases(self):
		return self.testcases
