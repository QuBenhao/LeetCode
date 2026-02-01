from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 2, 6, 4, 2], 3, 3], Output=5))
		self.testcases.append(case(Input=[[10, 1, 2, 2, 2, 1], 4, 3], Output=15))
		self.testcases.append(case(Input=[[10, 8, 18, 9], 3, 1], Output=36))

	def get_testcases(self):
		return self.testcases
