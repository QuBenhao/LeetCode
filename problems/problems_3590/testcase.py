from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-1, 0, 0], [1, 1, 1], [[0, 1], [0, 2], [0, 3]]], Output=[0, 1, -1]))
		self.testcases.append(case(Input=[[-1, 0, 1], [5, 2, 7], [[0, 1], [1, 2], [1, 3], [2, 1]]], Output=None))

	def get_testcases(self):
		return self.testcases
