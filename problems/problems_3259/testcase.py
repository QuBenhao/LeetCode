from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 1], [3, 1, 1]], Output=5))
		self.testcases.append(case(Input=[[4, 1, 1], [1, 1, 3]], Output=7))

	def get_testcases(self):
		return self.testcases
