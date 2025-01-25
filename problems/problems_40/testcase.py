from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 1, 2, 7, 6, 1, 5], 8], Output=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]))
		self.testcases.append(case(Input=[[2, 5, 2, 1, 2], 5], Output=[[1, 2, 2], [5]]))

	def get_testcases(self):
		return self.testcases
