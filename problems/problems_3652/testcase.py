from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 8], [-1, 0, 1], 2], Output=10))
		self.testcases.append(case(Input=[[5, 4, 3], [1, 1, 0], 2], Output=9))
		self.testcases.append(case(Input=[[5,8],[-1,-1],2], Output=8))

	def get_testcases(self):
		return self.testcases
