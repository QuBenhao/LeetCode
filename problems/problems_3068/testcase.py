from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 1], 3, [[0, 1], [0, 2]]], Output=6))
		self.testcases.append(case(Input=[[2, 3], 7, [[0, 1]]], Output=9))
		self.testcases.append(case(Input=[[7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]], Output=42))

	def get_testcases(self):
		return self.testcases
