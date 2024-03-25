from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Logger', 'shouldPrintMessage', 'shouldPrintMessage', 'shouldPrintMessage', 'shouldPrintMessage', 'shouldPrintMessage', 'shouldPrintMessage'], [[], [1, 'foo'], [2, 'bar'], [3, 'foo'], [8, 'bar'], [10, 'foo'], [11, 'foo']]], Output=[None, True, True, False, False, False, True]))

	def get_testcases(self):
		return self.testcases
