from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], Output=[3, 9, 20, None, None, 15, 7]))
		self.testcases.append(case(Input=[[-1], [-1]], Output=[-1]))
		self.testcases.append(case(Input=[[1,2,3],[3,2,1]], Output=[1,2,None,3]))

	def get_testcases(self):
		return self.testcases
