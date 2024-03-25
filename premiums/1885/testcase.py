from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 2, 1], [1, 2, 1, 2]], Output=1))
		self.testcases.append(case(Input=[[1, 10, 6, 2], [1, 4, 1, 5]], Output=5))

	def get_testcases(self):
		return self.testcases
