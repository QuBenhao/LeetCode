from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 2], Output=[1, 3]))
		self.testcases.append(case(Input=[2, 1, 1, 2], Output=[]))
		self.testcases.append(case(Input=[3, 2, 2, 1, 3, 2, 4], Output=[1, 4]))

	def get_testcases(self):
		return self.testcases
