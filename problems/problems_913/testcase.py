from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]], Output=0))
		self.testcases.append(case(Input=[[1, 3], [0], [3], [0, 2]], Output=1))
		self.testcases.append(case(Input=[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]], Output=0))

	def get_testcases(self):
		return self.testcases
