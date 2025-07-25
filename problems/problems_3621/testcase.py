from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 1], Output=2))
		self.testcases.append(case(Input=[7, 2], Output=3))

	def get_testcases(self):
		return self.testcases
