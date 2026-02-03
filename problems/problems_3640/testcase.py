from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, -2, -1, -3, 0, 2, -1], Output=-4))
		self.testcases.append(case(Input=[1, 4, 2, 7], Output=14))

	def get_testcases(self):
		return self.testcases
