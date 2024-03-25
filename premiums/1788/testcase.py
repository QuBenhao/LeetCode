from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 1, 2], Output=8))
		self.testcases.append(case(Input=[100, 1, 1, -3, 1], Output=3))
		self.testcases.append(case(Input=[-1, -2, 0, -1], Output=-2))

	def get_testcases(self):
		return self.testcases
