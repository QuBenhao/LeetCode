from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 2], Output=3))
		self.testcases.append(case(Input=[3, 3], Output=10))
		self.testcases.append(case(Input=[4, 1], Output=0))

	def get_testcases(self):
		return self.testcases
