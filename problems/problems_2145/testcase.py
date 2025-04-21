from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, -3, 4], 1, 6], Output=2))
		self.testcases.append(case(Input=[[3, -4, 5, 1, -2], -4, 5], Output=4))
		self.testcases.append(case(Input=[[4, -7, 2], 3, 6], Output=0))
		self.testcases.append(case(Input=[[-40],-46,53], Output=60))

	def get_testcases(self):
		return self.testcases
