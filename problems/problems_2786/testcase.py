from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 6, 1, 9, 2], 5], Output=13))
		self.testcases.append(case(Input=[[2, 4, 6, 8], 3], Output=20))

	def get_testcases(self):
		return self.testcases
