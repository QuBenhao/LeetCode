from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 5, 7], Output=[4, 5, 2, 7]))
		self.testcases.append(case(Input=[2, 3], Output=[2, 3]))

	def get_testcases(self):
		return self.testcases
