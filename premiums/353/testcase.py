from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['SnakeGame', 'move', 'move', 'move', 'move', 'move', 'move'], [[3, 2, [[1, 2], [0, 1]]], ['R'], ['D'], ['R'], ['U'], ['L'], ['U']]], Output=[None, 0, 0, 1, 1, 2, -1]))

	def get_testcases(self):
		return self.testcases
