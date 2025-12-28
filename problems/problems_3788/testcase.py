from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, -1, 3, -4, -5], Output=17))
		self.testcases.append(case(Input=[-7, -5, 3], Output=-2))
		self.testcases.append(case(Input=[1, 1], Output=0))

	def get_testcases(self):
		return self.testcases
