from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3], [3, 7], [8, 9]], Output=5))
		self.testcases.append(case(Input=[[1, 3], [1, 4], [2, 5], [3, 5]], Output=3))
		self.testcases.append(case(Input=[[1, 2], [2, 3], [2, 4], [4, 5]], Output=5))

	def get_testcases(self):
		return self.testcases
