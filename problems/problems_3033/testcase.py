from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, -1], [4, -1, 6], [7, 8, 9]], Output=[[1, 2, 9], [4, 8, 6], [7, 8, 9]]))
		self.testcases.append(case(Input=[[3, -1], [5, 2]], Output=[[3, 2], [5, 2]]))

	def get_testcases(self):
		return self.testcases
