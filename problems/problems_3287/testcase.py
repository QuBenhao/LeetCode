from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 6, 7], 1], Output=5))
		self.testcases.append(case(Input=[[4, 2, 5, 6, 7], 2], Output=2))

	def get_testcases(self):
		return self.testcases
