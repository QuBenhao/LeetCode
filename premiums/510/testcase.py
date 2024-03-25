from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 3], 1], Output=2))
		self.testcases.append(case(Input=[[5, 3, 6, 2, 4, None, None, 1], 6], Output=None))

	def get_testcases(self):
		return self.testcases
