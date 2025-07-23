from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]], Output=9))
		self.testcases.append(case(Input=[[5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]], Output=0))

	def get_testcases(self):
		return self.testcases
