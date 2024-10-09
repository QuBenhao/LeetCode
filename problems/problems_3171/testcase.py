from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 4, 5], 3], Output=0))
		self.testcases.append(case(Input=[[1, 3, 1, 3], 2], Output=1))
		self.testcases.append(case(Input=[[1], 10], Output=9))
		self.testcases.append(case(Input=[[3,50,1,29,27],66], Output=3))

	def get_testcases(self):
		return self.testcases
