from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 9, 7], 5], Output=4))
		self.testcases.append(case(Input=[[4, 1, 3], 4], Output=0))
		self.testcases.append(case(Input=[[3, 2], 6], Output=5))

	def get_testcases(self):
		return self.testcases
