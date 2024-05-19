from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], Output=5))
		self.testcases.append(case(Input=[[1, 2, 3], [2, 3, 4], [2, 3, 5]], Output=2))

	def get_testcases(self):
		return self.testcases
