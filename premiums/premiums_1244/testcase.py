from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Leaderboard', 'addScore', 'addScore', 'addScore', 'addScore', 'addScore', 'top', 'reset', 'reset', 'addScore', 'top'], [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2], [2, 51], [3]]], Output=[None, None, None, None, None, None, 73, None, None, None, 141]))

	def get_testcases(self):
		return self.testcases
