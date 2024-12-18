from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 2], Output=[3, 4]))
		self.testcases.append(case(Input=[[10, 1, 10, 1, 10], 3], Output=[1, 3]))
		self.testcases.append(case(Input=[[10, 1, 10, 1, 10], 10], Output=[]))

	def get_testcases(self):
		return self.testcases
