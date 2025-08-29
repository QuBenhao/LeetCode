from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 10, -5], Output=[5, 10]))
		self.testcases.append(case(Input=[8, -8], Output=[]))
		self.testcases.append(case(Input=[10, 2, -5], Output=[10]))

	def get_testcases(self):
		return self.testcases
