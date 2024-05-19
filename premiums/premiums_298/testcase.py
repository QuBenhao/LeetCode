from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, None, 3, 2, 4, None, None, None, 5], Output=3))
		self.testcases.append(case(Input=[2, None, 3, 2, None, 1], Output=2))

	def get_testcases(self):
		return self.testcases
