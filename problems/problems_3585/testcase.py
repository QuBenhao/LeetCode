from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [[0, 1, 7]], [[1, 0], [0, 1]]], Output=[0, 1]))
		self.testcases.append(case(Input=[3, [[0, 1, 2], [2, 0, 4]], [[0, 1], [2, 0], [1, 2]]], Output=[1, 0, 2]))
		self.testcases.append(case(Input=[5, [[0, 1, 2], [0, 2, 5], [1, 3, 1], [2, 4, 3]], [[3, 4], [1, 2]]], Output=[2, 2]))
		self.testcases.append(case(Input=[2,[[0,1,2]],[[1,1]]], Output=[1]))
		self.testcases.append(case(Input=[4,[[0,1,10],[1,2,1],[1,3,16]],[[3,2]]], Output=[1]))
		self.testcases.append(case(Input=[4,[[0,1,5],[1,2,14],[0,3,9]],[[2,0],[0,3]]], Output=[1,3]))

	def get_testcases(self):
		return self.testcases
