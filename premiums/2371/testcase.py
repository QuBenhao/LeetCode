from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 1], [2, 5]], Output=[[2, 1], [1, 2]]))
		self.testcases.append(case(Input=[[10]], Output=[[1]]))

	def get_testcases(self):
		return self.testcases
