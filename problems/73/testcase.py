from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], Output=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
		self.testcases.append(case(Input=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], Output=[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]))

	def get_testcases(self):
		return self.testcases
