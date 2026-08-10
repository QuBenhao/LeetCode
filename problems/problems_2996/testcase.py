from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 2, 5], Output=6))
		self.testcases.append(case(Input=[3, 4, 5, 1, 12, 14, 13], Output=15))

	def get_testcases(self):
		return self.testcases
