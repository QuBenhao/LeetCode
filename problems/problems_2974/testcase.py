from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 4, 2, 3], Output=[3, 2, 5, 4]))
		self.testcases.append(case(Input=[2, 5], Output=[5, 2]))

	def get_testcases(self):
		return self.testcases
