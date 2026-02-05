from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 5], 2], Output=1))
		self.testcases.append(case(Input=[[1, 6, 2, 9], 3], Output=2))
		self.testcases.append(case(Input=[[4, 6], 2], Output=0))

	def get_testcases(self):
		return self.testcases
