from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4], [3], [1, 10]], Output=1))
		self.testcases.append(case(Input=[[10, 2], [5, 1], [5, 2, 7]], Output=3))
		self.testcases.append(case(Input=[[1, 2], [100, 1], [10]], Output=0))

	def get_testcases(self):
		return self.testcases
