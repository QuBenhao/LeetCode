from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]], Output=[False, True, True]))
		self.testcases.append(case(Input=[[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]], Output=[True, True, False]))

	def get_testcases(self):
		return self.testcases
