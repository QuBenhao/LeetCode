from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 4], [1, 4, 7, 9]], Output=[1, 4]))
		self.testcases.append(case(Input=[[2, 3, 6, 8], [1, 2, 3, 5, 6, 7, 10], [2, 3, 4, 6, 9]], Output=[2, 3, 6]))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [6, 7, 8]], Output=[]))

	def get_testcases(self):
		return self.testcases
