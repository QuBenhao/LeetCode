from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']], Output=3))
		self.testcases.append(case(Input=[['B', 'B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'B']], Output=0))

	def get_testcases(self):
		return self.testcases
