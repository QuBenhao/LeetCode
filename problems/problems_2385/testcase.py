from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 5, 3, None, 4, 10, 6, 9, 2], 3], Output=4))
		self.testcases.append(case(Input=[[1], 1], Output=0))
		self.testcases.append(case(Input=[[2,3,None,4,1,None,None,None,5],1], Output=2))
		self.testcases.append(case(Input=[[5,2,3,4,None,None,None,1],4], Output=3))

	def get_testcases(self):
		return self.testcases
