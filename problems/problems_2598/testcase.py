from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, -10, 7, 13, 6, 8], 5], Output=4))
		self.testcases.append(case(Input=[[1, -10, 7, 13, 6, 8], 7], Output=2))
		self.testcases.append(case(Input=[[0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1],2], Output=15))

	def get_testcases(self):
		return self.testcases
