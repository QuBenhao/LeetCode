from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, -1], [1, -2, 3], [2, -3, 4]], Output=8))
		self.testcases.append(case(Input=[[10, 10, 10], [10, 10, 10]], Output=40))

	def get_testcases(self):
		return self.testcases
