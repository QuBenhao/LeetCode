from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 3, 6, 2, 4, None, 7], 3], Output=[5, 4, 6, 2, None, None, 7]))
		self.testcases.append(case(Input=[[5, 3, 6, 2, 4, None, 7], 0], Output=[5, 3, 6, 2, 4, None, 7]))
		self.testcases.append(case(Input=[[], 0], Output=[]))

	def get_testcases(self):
		return self.testcases
