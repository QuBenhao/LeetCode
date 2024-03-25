from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Excel', 'set', 'sum', 'set', 'get'], [[3, 'C'], [1, 'A', 2], [3, 'C', ['A1', 'A1:B2']], [2, 'B', 2], [3, 'C']]], Output=[None, None, 4, None, 6]))

	def get_testcases(self):
		return self.testcases
