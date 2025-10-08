from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 5, 2, 4], [5, 1, 4, 2]], Output=110))
		self.testcases.append(case(Input=[[1, 1, 1], [1, 1, 1]], Output=5))
		self.testcases.append(case(Input=[[1, 2, 3, 4], [1, 2]], Output=21))

	def get_testcases(self):
		return self.testcases
