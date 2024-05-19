from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 2, 3, 4], 2], Output=3))
		self.testcases.append(case(Input=[[5, 1, 4, 2, 2], 6], Output=0))

	def get_testcases(self):
		return self.testcases
