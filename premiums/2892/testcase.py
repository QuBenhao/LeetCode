from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 3, 7, 3, 5], 20], Output=3))
		self.testcases.append(case(Input=[[3, 3, 3, 3], 6], Output=4))

	def get_testcases(self):
		return self.testcases
