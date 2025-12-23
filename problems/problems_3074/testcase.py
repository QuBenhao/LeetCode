from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 2], [4, 3, 1, 5, 2]], Output=2))
		self.testcases.append(case(Input=[[5, 5, 5], [2, 4, 2, 7]], Output=4))

	def get_testcases(self):
		return self.testcases
