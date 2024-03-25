from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, 6, 5, 4, 3, 2, 1, 6, 10, 11], Output=8))
		self.testcases.append(case(Input=[57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63], Output=6))
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=0))

	def get_testcases(self):
		return self.testcases
