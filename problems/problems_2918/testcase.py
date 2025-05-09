from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 0, 1, 0], [6, 5, 0]], Output=12))
		self.testcases.append(case(Input=[[2, 0, 2, 0], [1, 4]], Output=-1))

	def get_testcases(self):
		return self.testcases
