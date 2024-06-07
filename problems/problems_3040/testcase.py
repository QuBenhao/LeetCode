from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2, 1, 2, 3, 4], Output=3))
		self.testcases.append(case(Input=[3, 2, 6, 1, 4], Output=2))

	def get_testcases(self):
		return self.testcases
