from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]], Output=14))
		self.testcases.append(case(Input=[[2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]], Output=11))

	def get_testcases(self):
		return self.testcases
