from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 2], [4, 5, 2], [2, 4, 3]], Output=4))
		self.testcases.append(case(Input=[[1, 3, 2], [4, 5, 2], [1, 5, 5]], Output=5))
		self.testcases.append(case(Input=[[1, 5, 3], [1, 5, 1], [6, 6, 5]], Output=8))
		self.testcases.append(case(Input=[[10,83,53],[63,87,45],[97,100,32],[51,61,16]], Output=85))

	def get_testcases(self):
		return self.testcases
