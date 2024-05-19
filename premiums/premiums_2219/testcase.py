from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 3, -2, 5], Output=10))
		self.testcases.append(case(Input=[-3, -5], Output=-3))

	def get_testcases(self):
		return self.testcases
