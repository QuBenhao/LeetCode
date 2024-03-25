from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9], Output=0.5))
		self.testcases.append(case(Input=[[23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1], Output=14.0))

	def get_testcases(self):
		return self.testcases
