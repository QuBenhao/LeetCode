from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 3, 4, 2], [4, 2, 2, 5]], Output=40))
		self.testcases.append(case(Input=[[2, 1, 4, 5, 7], [3, 2, 4, 8, 6]], Output=65))

	def get_testcases(self):
		return self.testcases
