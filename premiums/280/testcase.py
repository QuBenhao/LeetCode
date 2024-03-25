from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 5, 2, 1, 6, 4], Output=[3, 5, 1, 6, 2, 4]))
		self.testcases.append(case(Input=[6, 6, 5, 6, 3, 8], Output=[6, 6, 5, 6, 3, 8]))

	def get_testcases(self):
		return self.testcases
