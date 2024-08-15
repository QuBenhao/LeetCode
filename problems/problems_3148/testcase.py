from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]], Output=9))
		self.testcases.append(case(Input=[[4, 3, 2], [3, 2, 1]], Output=-1))
		self.testcases.append(case(Input=[[4,9],[5,2],[3,1]], Output=5))

	def get_testcases(self):
		return self.testcases
