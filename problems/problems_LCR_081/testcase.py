from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 6, 7], 7], Output=[[7], [2, 2, 3]]))
		self.testcases.append(case(Input=[[2, 3, 5], 8], Output=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]))
		self.testcases.append(case(Input=[[2], 1], Output=[]))

	def get_testcases(self):
		return self.testcases
