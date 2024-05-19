from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 1, 13, 6, 9, 5], 3, 4, [1000000, 1000001, 1000002]], Output=[10, 1, 13, 1000000, 1000001, 1000002, 5]))
		self.testcases.append(case(Input=[[0, 1, 2, 3, 4, 5, 6], 2, 5, [1000000, 1000001, 1000002, 1000003, 1000004]], Output=[0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]))

	def get_testcases(self):
		return self.testcases
