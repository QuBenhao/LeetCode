from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 1], [[0, 2, 1, 4]]], Output=4))
		self.testcases.append(case(Input=[[2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]], Output=31))

	def get_testcases(self):
		return self.testcases
