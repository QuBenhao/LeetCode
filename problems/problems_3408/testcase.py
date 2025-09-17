from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TaskManager', 'add', 'edit', 'execTop', 'rmv', 'add', 'execTop'], [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]], Output=[None, None, None, 3, None, None, 5]))

	def get_testcases(self):
		return self.testcases
