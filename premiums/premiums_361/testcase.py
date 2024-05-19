from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']], Output=3))
		self.testcases.append(case(Input=[['W', 'W', 'W'], ['0', '0', '0'], ['E', 'E', 'E']], Output=1))

	def get_testcases(self):
		return self.testcases
