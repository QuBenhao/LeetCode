from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, [[2, 3]], [[0, 2], [1, 0]]], Output=3))
		self.testcases.append(case(Input=[3, 2, [[3, 4, 2], [2, 1, 2]], [[0, 2, 1], [2, 0, 4], [3, 2, 0]]], Output=8))
		self.testcases.append(case(Input=[2,2,[[1,3],[4,1]],[[0,1],[5,0]]], Output=9))
		self.testcases.append(case(Input=[1,3,[[1],[2],[9]],[[0]]], Output=12))

	def get_testcases(self):
		return self.testcases
