from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4], 3], Output=4))
		self.testcases.append(case(Input=[[2, 2], 2], Output=0))
		self.testcases.append(case(Input=[[4, 3, -1], 2], Output=10))

	def get_testcases(self):
		return self.testcases
