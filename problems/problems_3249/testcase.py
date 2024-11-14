from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], Output=7))
		self.testcases.append(case(Input=[[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]], Output=6))
		self.testcases.append(case(Input=[[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]], Output=12))
		self.testcases.append(case(Input=[[2,0],[4,2],[1,2],[3,1],[5,1]], Output=5))

	def get_testcases(self):
		return self.testcases
