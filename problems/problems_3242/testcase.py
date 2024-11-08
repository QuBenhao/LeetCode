from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['NeighborSum', 'adjacentSum', 'adjacentSum', 'diagonalSum', 'diagonalSum'], [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]], Output=[None, 6, 16, 16, 4]))
		self.testcases.append(case(Input=[['NeighborSum', 'adjacentSum', 'diagonalSum'], [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]], Output=[None, 23, 45]))

	def get_testcases(self):
		return self.testcases
