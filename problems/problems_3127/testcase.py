from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'B']], Output=True))
		self.testcases.append(case(Input=[['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']], Output=False))
		self.testcases.append(case(Input=[['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'W']], Output=True))
		self.testcases.append(case(Input=[["B","B","B"],["B","B","B"],["B","B","B"]], Output=True))

	def get_testcases(self):
		return self.testcases
