from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TreeAncestor', 'getKthAncestor', 'getKthAncestor', 'getKthAncestor'], [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]], Output=[None, 1, 0, -1]))
		self.testcases.append(case(Input=[["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"],[[10,[-1,0,0,1,2,0,1,3,6,1]],[8,6],[9,7],[1,1],[2,5],[4,2],[7,3],[3,7],[9,6],[3,5],[8,8]]], Output=[None,-1,-1,0,-1,0,0,-1,-1,-1,-1]))

	def get_testcases(self):
		return self.testcases
