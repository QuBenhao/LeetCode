from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 2, 2, 4, 3], 3], Output=2))
		self.testcases.append(case(Input=[[7, 3, 4, 7], 7], Output=2))
		self.testcases.append(case(Input=[[4, 3, 2, 6, 2, 3, 4], 6], Output=-1))

	def get_testcases(self):
		return self.testcases
