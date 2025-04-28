from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['h', 'e', 'l', 'l', 'o'], Output=['o', 'l', 'l', 'e', 'h']))
		self.testcases.append(case(Input=['H', 'a', 'n', 'n', 'a', 'h'], Output=['h', 'a', 'n', 'n', 'a', 'H']))

	def get_testcases(self):
		return self.testcases
