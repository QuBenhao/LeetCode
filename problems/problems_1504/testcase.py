from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 0, 1], [1, 1, 0], [1, 1, 0]], Output=13))
		self.testcases.append(case(Input=[[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]], Output=24))
		self.testcases.append(case(Input=[[0,1,1,0,0,0,1,1,1,0],[1,1,1,0,1,0,0,1,0,1],[0,1,1,1,0,1,1,1,0,0],[0,1,0,0,1,1,1,1,1,0],[0,0,1,1,0,1,1,1,0,1],[0,0,1,0,1,0,0,1,1,1],[1,0,1,0,0,1,1,1,0,1],[1,0,1,1,0,0,1,1,1,0],[0,0,1,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,1]], Output=209))
		self.testcases.append(case(Input=[[0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1],[0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],[1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1],[0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0],[1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],[1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1],[1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1],[0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1],[1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0]], Output=1389))

	def get_testcases(self):
		return self.testcases
