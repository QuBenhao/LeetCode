from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 7], 3], Output=3))
		self.testcases.append(case(Input=[[5, 4, 3, 2, 1, 1000000000], 2], Output=999999999))

	def get_testcases(self):
		return self.testcases
