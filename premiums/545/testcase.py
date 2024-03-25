from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, None, 2, 3, 4], Output=[1, 3, 4, 2]))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10], Output=[1, 2, 4, 7, 8, 9, 10, 6, 3]))

	def get_testcases(self):
		return self.testcases
