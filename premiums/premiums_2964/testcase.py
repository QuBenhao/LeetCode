from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 3, 4, 7, 8], 5], Output=3))
		self.testcases.append(case(Input=[[3, 3, 3, 3], 3], Output=4))
		self.testcases.append(case(Input=[[3, 3, 3, 3], 6], Output=0))

	def get_testcases(self):
		return self.testcases
