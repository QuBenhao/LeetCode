from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']], 3], Output=6))
		self.testcases.append(case(Input=[[['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']], 1], Output=0))

	def get_testcases(self):
		return self.testcases
