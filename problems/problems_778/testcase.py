from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 2], [1, 3]], Output=3))
		self.testcases.append(case(Input=[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], Output=16))
		self.testcases.append(case(Input=[[3,2],[0,1]], Output=3))

	def get_testcases(self):
		return self.testcases
