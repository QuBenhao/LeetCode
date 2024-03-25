from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 5, 2, 4], [2, 1, 2, 4, 3], [10, 20, 30, 40, 50]], Output=None))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [2, 4, 3, 3, 1], [10, 20, 30, 40, 40]], Output=None))

	def get_testcases(self):
		return self.testcases
