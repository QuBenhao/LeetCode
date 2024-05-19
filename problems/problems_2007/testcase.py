from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3, 4, 2, 6, 8], Output=[1, 3, 4]))
		self.testcases.append(case(Input=[6, 3, 0, 1], Output=[]))
		self.testcases.append(case(Input=[1], Output=[]))

	def get_testcases(self):
		return self.testcases
