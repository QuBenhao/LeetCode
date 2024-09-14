from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8], Output=3))
		self.testcases.append(case(Input=[[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], Output=3))
		self.testcases.append(case(Input=[[715827882,715827882,None,715827882,None,1,None,715827882,None,715827882,None,715827882,None],-3], Output=0))
		self.testcases.append(case(Input=[[1,-2,-3],-1], Output=1))
		self.testcases.append(case(Input=[[1],0], Output=0))

	def get_testcases(self):
		return self.testcases
