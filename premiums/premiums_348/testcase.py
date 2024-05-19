from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TicTacToe', 'move', 'move', 'move', 'move', 'move', 'move', 'move'], [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]], Output=[None, 0, 0, 0, 0, 0, 0, 1]))

	def get_testcases(self):
		return self.testcases
