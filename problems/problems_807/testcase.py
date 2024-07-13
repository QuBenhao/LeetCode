from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]], Output=35))
		self.testcases.append(case(Input=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], Output=0))

	def get_testcases(self):
		return self.testcases
