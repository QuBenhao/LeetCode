from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 6, 9], 3], Output=9))
		self.testcases.append(case(Input=[[5, 2], 7], Output=12))

	def get_testcases(self):
		return self.testcases
