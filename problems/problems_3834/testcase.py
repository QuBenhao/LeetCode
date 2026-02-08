from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 1, 1, 2], Output=[3, 4]))
		self.testcases.append(case(Input=[2, 2, 4], Output=[8]))
		self.testcases.append(case(Input=[3, 7, 5], Output=[3, 7, 5]))

	def get_testcases(self):
		return self.testcases
