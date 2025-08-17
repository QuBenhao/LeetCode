from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]], Output=5))
		self.testcases.append(case(Input=[4, [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]], Output=3))
		self.testcases.append(case(Input=[2,[[0,1,17],[1,0,12]]], Output=17))

	def get_testcases(self):
		return self.testcases
