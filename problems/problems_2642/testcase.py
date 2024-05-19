from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Graph', 'shortestPath', 'shortestPath', 'addEdge', 'shortestPath'], [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]], Output=[None, 6, -1, None, 6]))

	def get_testcases(self):
		return self.testcases
