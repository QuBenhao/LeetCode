from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, 2, 4], Output=5))
		self.testcases.append(case(Input=[4, 1, 3], Output=6))

	def get_testcases(self):
		return self.testcases
