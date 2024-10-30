from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 9], [[1, -2], [0, -3]]], Output=21))
		self.testcases.append(case(Input=[[0, -1], [[0, -5]]], Output=0))

	def get_testcases(self):
		return self.testcases
