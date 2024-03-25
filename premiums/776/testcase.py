from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 6, 1, 3, 5, 7], 2], Output=[[2, 1], [4, 3, 6, None, None, 5, 7]]))
		self.testcases.append(case(Input=[[1], 1], Output=[[1], []]))

	def get_testcases(self):
		return self.testcases
