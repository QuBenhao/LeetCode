from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], Output=15))
		self.testcases.append(case(Input=[[1, 0, 1], [1, 1, 0], [1, 1, 0]], Output=7))

	def get_testcases(self):
		return self.testcases
