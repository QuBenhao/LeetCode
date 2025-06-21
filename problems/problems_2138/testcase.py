from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcdefghi', 3, 'x'], Output=['abc', 'def', 'ghi']))
		self.testcases.append(case(Input=['abcdefghij', 3, 'x'], Output=['abc', 'def', 'ghi', 'jxx']))

	def get_testcases(self):
		return self.testcases
