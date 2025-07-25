from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]], Output=[3, 2, 3]))
		self.testcases.append(case(Input=[3, [], [[1, 1], [2, 1], [1, 1]]], Output=[1, -1]))
		self.testcases.append(case(Input=[3,[[3,2],[1,3],[2,1]],[[2,2],[1,2],[1,2],[1,3],[1,1],[1,3],[1,1],[1,1],[2,1],[1,1],[2,3],[2,3],[2,3],[2,1],[2,1],[2,1],[1,1],[1,1],[1,2],[1,2],[2,1],[2,1],[2,2],[1,2],[1,1]]], Output=[1,1,3,1,3,1,1,3,-1,-1,-1,-1,-1,-1]))

	def get_testcases(self):
		return self.testcases
