from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]], Output=16))
		self.testcases.append(case(Input=[[1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [[1, 2, 3, 4, 5], [], [], [], [], []], [[1, 2, 3, 4, 5], [], [], [], [], []], [0]], Output=6))

	def get_testcases(self):
		return self.testcases
