from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 2, 4], [1, 7, 5]], Output=2))
		self.testcases.append(case(Input=[[3, 18, 15, 9], [6, 5, 1, 3]], Output=3))

	def get_testcases(self):
		return self.testcases
