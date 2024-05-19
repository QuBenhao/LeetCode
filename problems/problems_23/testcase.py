from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 5], [1, 3, 4], [2, 6]], Output=[1, 1, 2, 3, 4, 4, 5, 6]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[[]], Output=[]))

	def get_testcases(self):
		return self.testcases
