from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 0, 2], [[0, 2], [0, 2], [1, 1]]], Output=1))
		self.testcases.append(case(Input=[[1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]], Output=2))
		self.testcases.append(case(Input=[[1, 2, 3, 4], [[0, 3]]], Output=-1))

	def get_testcases(self):
		return self.testcases
