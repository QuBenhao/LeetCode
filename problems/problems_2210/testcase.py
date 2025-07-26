from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 4, 1, 1, 6, 5], Output=3))
		self.testcases.append(case(Input=[6, 6, 5, 5, 4, 1], Output=0))

	def get_testcases(self):
		return self.testcases
