from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]], Output=[[1, 2, 10], [4, 5, 7, 8]]))
		self.testcases.append(case(Input=[[2, 3], [1, 3], [5, 4], [6, 4]], Output=[[1, 2, 5, 6], []]))

	def get_testcases(self):
		return self.testcases
