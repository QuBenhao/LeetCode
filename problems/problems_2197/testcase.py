from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, 4, 3, 2, 7, 6, 2], Output=[12, 7, 6]))
		self.testcases.append(case(Input=[2, 2, 1, 1, 3, 3, 3], Output=[2, 1, 1, 3]))

	def get_testcases(self):
		return self.testcases
