from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 5, 15, 1, 8, None, 7], Output=3))
		self.testcases.append(case(Input=[4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1], Output=2))

	def get_testcases(self):
		return self.testcases
