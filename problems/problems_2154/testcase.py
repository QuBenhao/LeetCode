from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 3, 6, 1, 12], 3], Output=24))
		self.testcases.append(case(Input=[[2, 7, 9], 4], Output=4))

	def get_testcases(self):
		return self.testcases
