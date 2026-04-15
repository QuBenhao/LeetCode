from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 1, 4, 1, 3, 2], [0, 3, 5]], Output=[2, -1, 3]))
		self.testcases.append(case(Input=[[1, 2, 3, 4], [0, 1, 2, 3]], Output=[-1, -1, -1, -1]))
		self.testcases.append(case(Input=[[6,12,17,9,16,7,6],[5,6,0,4]], Output=[-1,1,1,-1]))
		self.testcases.append(case(Input=[[1,3,1,4,1,3,2],[0,3,5]], Output=[2,-1,3]))

	def get_testcases(self):
		return self.testcases
