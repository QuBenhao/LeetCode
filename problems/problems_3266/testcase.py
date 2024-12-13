from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 3, 5, 6], 5, 2], Output=[8, 4, 6, 5, 6]))
		self.testcases.append(case(Input=[[100000, 2000], 2, 1000000], Output=[999999307, 999999993]))

	def get_testcases(self):
		return self.testcases
