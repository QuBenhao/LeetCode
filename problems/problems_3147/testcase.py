from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 2, -10, -5, 1], 3], Output=3))
		self.testcases.append(case(Input=[[-2, -3, -1], 2], Output=-1))

	def get_testcases(self):
		return self.testcases
