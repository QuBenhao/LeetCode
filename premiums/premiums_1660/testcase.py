from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], 2, 3], Output=[1, None, 3]))
		self.testcases.append(case(Input=[[8, 3, 1, 7, None, 9, 4, 2, None, None, None, 5, 6], 7, 4], Output=[8, 3, 1, None, None, 9, 4, None, None, 5, 6]))

	def get_testcases(self):
		return self.testcases
