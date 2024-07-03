from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1], [3, 2, 5], [5, 4]], Output=[3, 2, 5, 1, None, 4]))
		self.testcases.append(case(Input=[[5, 3, 8], [3, 2, 6]], Output=[]))
		self.testcases.append(case(Input=[[5, 4], [3]], Output=[]))

	def get_testcases(self):
		return self.testcases
