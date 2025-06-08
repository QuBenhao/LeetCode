from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 4, 1, 3, 7], 4], Output=6))
		self.testcases.append(case(Input=[[3, 3, 4], 0], Output=2))

	def get_testcases(self):
		return self.testcases
