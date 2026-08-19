from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 3], Output=[2, 3, 1]))
		self.testcases.append(case(Input=[5, 4, 3, 8], Output=[5, 3, 4, 8]))

	def get_testcases(self):
		return self.testcases
