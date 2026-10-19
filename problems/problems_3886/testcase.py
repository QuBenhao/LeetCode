from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 1, 2], Output=3))
		self.testcases.append(case(Input=[7, 6, 5], Output=0))
		self.testcases.append(case(Input=[5, 8], Output=3))

	def get_testcases(self):
		return self.testcases
